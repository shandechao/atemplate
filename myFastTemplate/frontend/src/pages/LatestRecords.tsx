
import React, { useState } from 'react';
import axios from 'axios';

type Record = {
  id: number;
  name: string;
  category: string;
  value: number;
  quantity: number;
  timestamp: string;
};

const LatestRecords: React.FC = () => {

    const [count, setCount] = useState(5);
    const [records, setRecords] = useState<Record[]>([]);

    const handleClick = async () => {
        try {
            const res = await axios.get(`http://localhost:8000/api/records/${count}`);
            setRecords(res.data);
        } catch (err) {
            alert('❌ 拉取失败');
        }
    };

  return (
    <div>
      <h2>📉 LatestRecords Data</h2>
      <p>LatestRecords results will appear here...</p>
    <hr></hr>
        
        <div className="input-group mb-3">
            <input 
            type="number" 
            className="form-control" 
            value={count} 
            onChange={(e) => setCount(Number(e.target.value))}
            />
            <button className="btn btn-primary" onClick={handleClick}>get data</button>
        </div>

        <ul className="list-group">
            {records.map((rec) => (
            <li key={rec.id} className="list-group-item">
                <strong>{rec.name}</strong> | {rec.category} | {rec.value} | {rec.quantity} | {new Date(rec.timestamp).toLocaleString()}
            </li>
            ))}
        </ul>
        

    </div>
  );
}

export default LatestRecords