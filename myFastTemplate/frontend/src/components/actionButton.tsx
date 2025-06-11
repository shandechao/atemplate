//import { Link } from 'react-router-dom'
import React, { useState } from 'react';

const ActionButtons: React.FC = ()=> {

    const [count, setCount] = useState(1); // 默认值是 1

    const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
        setCount(prev => prev + 1); // 每次点击 +1
        const value = event.currentTarget.getAttribute('data-myvalue');
        alert(`xxxxx ${value}`)
    };
    return (
    <>
        <button className='btn btn-success' onClick={handleClick} data-myvalue='adfadsf'>    aaa   {count}</button>
    </>
    )
}

export default ActionButtons
