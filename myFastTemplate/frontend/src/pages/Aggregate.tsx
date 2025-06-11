
import React, { useEffect, useRef, useState } from "react";
import D3plot from "../components/plot";

interface RecordData {
  name: string;
  avg_value: number;
}
var aa= 5;


const Aggregate: React.FC = () => {
  const [data, setData] = useState<RecordData[]>([]);
  const [filteredData, setFilteredData] = useState<RecordData[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [currentFilter, setCurrentFilter] = useState<string[] | null>(null);
  const [nowTime, setNowTime] = useState<string>("");
     
    
    useEffect(() => {
    const interval = setInterval(() => {
      fetch("http://localhost:8000/api/records/stock/aggregate")
        .then(res => res.json())
        .then(json => {
          setData(json);
          setNowTime(new Date().toLocaleTimeString());


            if (currentFilter && currentFilter.length > 0) {
                const filtered = json.filter(item =>currentFilter.includes(item.name.toUpperCase()));
                setFilteredData(filtered);
            } else {
                setFilteredData(json); 
            }
        });
        }, 1000);
        return () => clearInterval(interval);
     }, [currentFilter]);
    // End of useEffect

    const handleFilter = () => {
        const filters = inputValue
        .split(",")
        .map(s => s.trim().toUpperCase())
        .filter(Boolean);

        if (filters.length === 0) {
        setCurrentFilter(null); 
        } else {
        setCurrentFilter(filters); 
        }
    };

   
    return (
    <div>
      <h3 className="mb-3">当前时间：{nowTime}</h3>

      <div className="input-group mb-4" style={{ maxWidth: 400 }}>
        <input
          type="text"
          className="form-control"
          placeholder="AAPL, TSLA, MSFT"
          value={inputValue}
          onChange={e => setInputValue(e.target.value)}
        />
        <button className="btn btn-primary" onClick={handleFilter}>
          filter
        </button>
      </div>
      
      <div>
       {aa===4 && (
        <pre style={{ background: "#f8f9fa", padding: "10px", borderRadius: "5px" }}>
            {JSON.stringify(filteredData, null, 2)}
        </pre>
        )}

        {aa===5 && (
         <D3plot data={filteredData} />
        )}
      </div>
      
    </div>
  );
}

export default Aggregate

