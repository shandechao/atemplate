
import { Link } from 'react-router-dom'
import ActionButtons from '../components/actionButton'

const Home = () => {
  return (
    <div className="container mt-5">
      <h1>📊 Hello This is a demo  hello demo</h1>
      
      <Link to="/latest" className="btn btn-primary me-3">recent record</Link>
      <Link to="/aggregate" className="btn btn-secondary">look agg</Link>

      <div className='card'>

        <ActionButtons />
      </div>
    </div>
  )
}

export default Home