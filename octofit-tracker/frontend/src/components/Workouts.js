
import React, { useEffect, useState } from 'react';

function renderTable(data) {
  if (!data.length) return <tbody><tr><td colSpan="100%">No workouts found.</td></tr></tbody>;
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

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/workouts/`
    : '/api/workouts/';

  useEffect(() => {
    console.log('Fetching workouts from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Fetched workouts:', results);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, [endpoint]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Workouts</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered table-hover">
            {renderTable(workouts)}
          </table>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
