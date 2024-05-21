import React, { useState, useEffect } from 'react'



function App(){
  
  const [data, setData] = useState([{

  }])

  useEffect(() => {
    fetch("/api/v1/roles").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div>
      <h3>Roles</h3>
      {(typeof data.roles === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.roles.map((role, i) => (
          <p key={i}>{role}</p>
        )
      )
      )}
    </div>
  )
}

export default App