import React, { useState, useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import './App.css';

export default function App() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: 'bot',
      text: "Hello! Ask me anything about Shiven's resume, or **upload a Job Description (PDF/DOCX)** using the attachment button below to run an instant match score analysis!",
    },
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const messagesEndRef = useRef(null);
  const fileInputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  // Handle standard message streaming
  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userQuery = input.trim();
    setInput('');
    setIsLoading(true);

    const userMsgId = Date.now();
    const botMsgId = Date.now() + 1;

    setMessages((prev) => [
      ...prev,
      { id: userMsgId, sender: 'user', text: userQuery },
      { id: botMsgId, sender: 'bot', text: '' },
    ]);

    await streamResponse('http://127.0.0.1:8000/chat', JSON.stringify({ message: userQuery }), 'application/json', botMsgId);
  };

  // Handle file upload & JD matching
  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file || isLoading) return;

    setIsLoading(true);
    const userMsgId = Date.now();
    const botMsgId = Date.now() + 1;

    setMessages((prev) => [
      ...prev,
      { id: userMsgId, sender: 'user', text: `📁 Uploaded Job Description: **${file.name}**` },
      { id: botMsgId, sender: 'bot', text: '' },
    ]);

    const formData = new FormData();
    formData.append('file', file);

    // Reset file input value so same file can be uploaded again if needed
    e.target.value = '';

    await streamResponse('http://127.0.0.1:8000/chat/match-jd', formData, null, botMsgId);
  };

  // Shared streaming response consumer
  const streamResponse = async (url, body, contentType, botMsgId) => {
    try {
      const headers = {};
      if (contentType) headers['Content-Type'] = contentType;

      const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: body,
      });

      if (!response.body) throw new Error('No response body');

      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value, { stream: true });

        setMessages((prev) =>
          prev.map((msg) =>
            msg.id === botMsgId ? { ...msg, text: msg.text + chunk } : msg
          )
        );
      }
    } catch (error) {
      console.error('Error during streaming:', error);
      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === botMsgId
            ? { ...msg, text: '⚠️ Unable to complete request. Please try again.' }
            : msg
        )
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-viewport">
      <div className="glass-chat-card">
        {/* Header */}
        <header className="glass-header">
          <div className="brand">
            <div className="sparkle-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M12 2L14.5 9.5L22 12L14.5 14.5L12 22L9.5 14.5L2 12L9.5 9.5L12 2Z" />
              </svg>
            </div>
            <div>
              <h3>Candidate Insights & Matcher</h3>
              <p className="subtitle">Resume Chatbot & JD Fit Analyzer</p>
            </div>
          </div>
          <div className="status-pill">
            <span className="online-dot"></span> Live
          </div>
        </header>

        {/* Message Feed */}
        <div className="messages-container">
          {messages.map((msg) => (
            <div
              key={msg.id}
              className={`message-row ${msg.sender === 'user' ? 'user-row' : 'bot-row'}`}
            >
              {msg.sender === 'bot' && <div className="avatar bot-avatar">🤖</div>}

              <div className={`glass-bubble ${msg.sender === 'user' ? 'user-bubble' : 'bot-bubble'}`}>
                {msg.text === '' && isLoading && msg.sender === 'bot' ? (
                  <div className="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                ) : (
                  <div className="markdown-content">
                    <ReactMarkdown>{msg.text}</ReactMarkdown>
                  </div>
                )}
              </div>

              {msg.sender === 'user' && <div className="avatar user-avatar">👤</div>}
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Bar with Attachment */}
        <form onSubmit={handleSend} className="glass-input-wrapper">
          {/* Hidden File Input */}
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileUpload}
            accept=".pdf,.docx"
            style={{ display: 'none' }}
          />

          {/* Paperclip Button */}
          <button
            type="button"
            className="attach-btn"
            onClick={() => fileInputRef.current?.click()}
            disabled={isLoading}
            title="Upload JD (.pdf or .docx)"
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path>
            </svg>
          </button>

          <input
            type="text"
            placeholder="Ask a question or upload a JD to match..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            disabled={isLoading}
          />

          <button type="submit" className="send-btn" disabled={isLoading || !input.trim()}>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <line x1="22" y1="2" x2="11" y2="13"></line>
              <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
            </svg>
          </button>
        </form>
      </div>
    </div>
  );
}