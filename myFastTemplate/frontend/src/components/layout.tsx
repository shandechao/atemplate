import { Link } from "react-router-dom";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="container">
      <nav className="navbar-brand" style={{ padding: "10px", borderBottom: "1px solid #ccc" }}>
        <Link to="/" style={{ marginRight: "10px" }}>Home</Link>
        <Link to="/latest" style={{ marginRight: "10px" }}>Latest</Link>
        <Link to="/aggregate">Aggregate</Link>
        
      </nav>
      <div style={{ padding: "20px" }}>
        {children}
      </div>
    </div>
  );
}