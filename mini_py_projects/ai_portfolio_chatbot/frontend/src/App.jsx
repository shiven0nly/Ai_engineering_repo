import React, { useState, useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import './App.css';

export default function App() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: 'bot',
      text: "Hello! Ask me anything about Shiven's resume, upload a Job Description, or click the **mic icon** to speak your question!",
    },
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isListening, setIsListening] = useState(false);

  const messagesEndRef = useRef(null);
  const fileInputRef = useRef(null);
  const recognitionRef = useRef(null);

  // Initialize Speech Recognition on component mount
  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
      const recognition = new SpeechRecognition();
      recognition.continuous = true;
      recognition.interimResults = true;
      recognition.lang = 'en-US';

      recognition.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
          transcript += event.results[i][0].transcript;
        }
        setInput(transcript);
      };

      recognition.onerror = (event) => {
        console.error('Speech recognition error:', event.error);
        setIsListening(false);
      };

      recognition.onend = () => {
        setIsListening(false);
      };

      recognitionRef.current = recognition;
    }
  }, []);

  const toggleListening = () => {
    if (!recognitionRef.current) {
      alert('Voice recognition is not supported in this browser. Please use Chrome, Edge, or Safari.');
      return;
    }

    if (isListening) {
      recognitionRef.current.stop();
      setIsListening(false);
    } else {
      recognitionRef.current.start();
      setIsListening(true);
    }
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    // Stop listening if user sends while mic is active
    if (isListening) {
      recognitionRef.current?.stop();
      setIsListening(false);
    }

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

    await streamResponse('https://ai-engineering-repo.vercel.app/chat', JSON.stringify({ message: userQuery }), 'application/json', botMsgId);
  };

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
    e.target.value = '';

    await streamResponse('https://ai-engineering-repo.vercel.app/chat/match-jd', formData, null, botMsgId);
  };

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
      console.error('Streaming error:', error);
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

        {/* Input Bar with Attachment & Mic */}
        <form onSubmit={handleSend} className="glass-input-wrapper">
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileUpload}
            accept=".pdf,.docx"
            style={{ display: 'none' }}
          />

          {/* Attach File Button */}
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

          {/* Voice to Text Button */}
          <button
            type="button"
            className={`mic-btn ${isListening ? 'listening' : ''}`}
            onClick={toggleListening}
            disabled={isLoading}
            title={isListening ? 'Stop Listening' : 'Voice Input'}
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path>
              <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
              <line x1="12" y1="19" x2="12" y2="23"></line>
              <line x1="8" y1="23" x2="16" y2="23"></line>
            </svg>
          </button>

          <input
            type="text"
            placeholder={isListening ? 'Listening to your voice...' : 'Ask a question or upload a JD to match...'}
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