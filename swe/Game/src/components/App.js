import React, { useEffect, useState } from "react";

function App() {
  const [gameState, setGameState] = useState({
    player: "X",
    board: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    result: "",
  });

  useEffect(() => {
    fetch("/api/submit-move")
      .then((response) => response.json())
      .then((data) => setGameState(data.gameState));
  }, []);

  const handleClick = (index) => {
    if (gameState.board[index] === 0 && !gameState.result) {
      let board = gameState.board.slice();
      board[index] = gameState.player;
      const data = fetch("http://localhost:5000/api/submit-move", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ move: index }),
      })
        .then((response) => response.json())
        .then((data) => setGameState(data.gameState));
    }
  };

  const renderCell = (index) => {
    let value = "";
    if (gameState.board[index] === "X") {
      value = "X";
    } else if (gameState.board[index] === "O") {
      value = "O";
    }
    return (
      <div className="cell" onClick={() => handleClick(index)}>
        {value}
      </div>
    );
  };

  const handleReset = () => {
    setGameState({
      player: "X",
      board: [0, 0, 0, 0, 0, 0, 0, 0, 0],
      result: "",
    });
  };

  return (
    <div className="game">
      <div className="board">
        {renderCell(0)}
        {renderCell(1)}
        {renderCell(2)}
        {renderCell(3)}
        {renderCell(4)}
        {renderCell(5)}
        {renderCell(6)}
        {renderCell(7)}
        {renderCell(8)}
      </div>
      <div className="status">
        {gameState.result ? gameState.result : `Player ${gameState.player}'s turn`}
      </div>
      <button onClick={handleReset}>Reset Game</button>
    </div>
  );
}

export default App;
