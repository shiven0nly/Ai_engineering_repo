import React, { useState, useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import './App.css';

export default function App() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: 'bot',
      text: "Hello! I'm your AI representative of Shiven Sharma. Ask me anything about Shiven's skills, experience, or projects!",
    },
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

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

    try {
      const response = await fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userQuery }),
      });

      if (!response.body) throw new Error('No stream response body.');

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
            ? { ...msg, text: '⚠️ Unable to reach server. Please try again.' }
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
              <h3>Candidate Insights</h3>
              <p className="subtitle">Powered by Groq & Gemini Prompt Architecture</p>
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
              {msg.sender === 'bot' && (
                <div className="avatar bot-avatar">
                  🤖
                </div>
              )}

              <div className={`glass-bubble ${msg.sender === 'user' ? 'user-bubble' : 'bot-bubble'}`}>
                {msg.text === '' && isLoading && msg.sender === 'bot' ? (
                  <div className="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                ) : msg.sender === 'bot' ? (
                  <div className="markdown-content">
                    <ReactMarkdown>{msg.text}</ReactMarkdown>
                  </div>
                ) : (
                  <p>{msg.text}</p>
                )}
              </div>

              {msg.sender === 'user' && (
                <div className="avatar user-avatar">
                  👤
                </div>
              )}
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Bar */}
        <form onSubmit={handleSend} className="glass-input-wrapper">
          <input
            type="text"
            placeholder="Ask about candidate experience, tech stack, projects..."
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