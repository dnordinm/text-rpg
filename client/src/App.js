import { useState, useEffect } from "react";

function App() {
  
  const [history, setHistory] = useState([]);
  const [input, setInput] = useState("");
  
  async function sendCommand(text = input) {
    const response = await fetch('http://localhost:5555/command', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text }),
    });
    const data = await response.json();
    console.log(data)
    setHistory([...history, input, data]);
    setInput('');
  }
  
  useEffect(() => {
    sendCommand("look");
  }, []);

  function renderLine(line, i) {
    if (typeof line === "string") {
      return <p key={i} style={{ color: "lime" }}>{line}</p>;
    }
    if (line.type === "look") {
      return (
        <div key={i}>
          <p style={{ color: "black" }}>{line.description}</p>
          <p style={{ color: "yellow" }}>Items: {line.items.join(", ")}</p>
          <p style={{ color: "cyan" }}>Exits: {line.exits.join(", ")}</p>
        </div>
      );
    }
    if (line.type === "move") {
      return <p key={i} style={{ color: "black" }}>{line.description}</p>;
    }
    if (line.type === "take") {
      return <p key={i} style={{ color: "green" }}>{line.message}</p>;
    }
    if (line.type === "error") {
      return <p key={i} style={{ color: "red" }}>{line.message}</p>;
    }
  }

  return (
    <div>
      <div>
        {history.map((line, i) => renderLine(line, i))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter command..."
      />
      <button onClick={() => sendCommand()}>Submit</button>
    </div>
  );
}

export default App;