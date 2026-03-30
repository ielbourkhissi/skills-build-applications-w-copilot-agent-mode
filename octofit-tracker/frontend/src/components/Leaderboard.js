
import React, { useEffect, useState } from 'react';

function renderTable(data) {
  if (!data.length) return <tbody><tr><td colSpan="100%">No leaderboard data found.</td></tr></tbody>;
  const columns = Object.keys(data[0]);
  return (
    <>
      <thead>
        <tr>
          {columns.map(col => <th key={col}>{col}</th>)}
        </tr>
      </thead>
      <tbody>
        {data.map((row, idx) => (
          <tr key={row.id || idx}>
            {columns.map(col => <td key={col}>{row[col]}</td>)}
          </tr>
        ))}
      </tbody>
    </>
  );
}

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/leaderboards/`
    : '/api/leaderboards/';

  useEffect(() => {
    console.log('Fetching leaderboard from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboard(results);
        console.log('Fetched leaderboard:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [endpoint]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Leaderboard</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered table-hover">
            {renderTable(leaderboard)}
          </table>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
