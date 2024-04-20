import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [textInput, setTextInput] = useState('');
  const [results, setResults] = useState([]);

  const handleSubmit = async (event) => {
    
    event.preventDefault();
    
    try {
      const response = await axios.post('http://localhost:5000/analyze', {
        comment: textInput
      });
      
      if (!response) {
        throw new Error('Failed to fetch data');
      }

      const data = response.data;
      const data1 = data.results;
      console.log(data1);
      setResults(data1);
      console.log(results);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleTextInputChange = (event) => {
    setTextInput(event.target.value);
  };

  return (
    <div className="App">
      <h1>Sentiment Analysis Tool</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={textInput}
          onChange={handleTextInputChange}
          placeholder="Enter text here..."
          rows={4}
          cols={50}
          required
        />
        <br />
        <button type="submit">Analyze</button>
      </form>
      <div className="results">
        {results.map((r,ind)=>{
          return (
            <>
            <div key={ind} className='result'>
              <p>Model : {ind+1}</p>
              <p>Results : {r}</p>
            </div>
            <div key={ind+1} className='result'>
            <p>Model : {ind+2}</p>
            <p>Results : {r}</p>
          </div>
          <div key={ind+2} className='result'>
          <p>Model : {ind+3}</p>
          <p>Results : {r}</p>
        </div>
        </>
          )
        })}
      </div>
    </div>
  );
}

export default App;
