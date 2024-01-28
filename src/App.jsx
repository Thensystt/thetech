import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Route, Routes, Link, NavLink } from "react-router-dom"
import halykLogo from './assets/halyk.png'

function Home() {
  return(
    <>
      <p>Home Page</p>
    </>
  );
}

function Chatbot() {
  return(
    <>
      <p>Chatbot</p>
      <div>
        <div>
          <p>Username</p>
          <p>Textcontent</p>
        </div>
      </div>
      <div>
        <input></input>
        <button >Prompt</button>
      </div>
    </>
  );
}

function Calculator() {
  const [inputValue, setInputValue] = useState('');
  const [valueFromDurationPeriod, setValueFromDurationPeriod] = useState('');
  const [result, setResult] = useState(null);

  const handleInputChange = (e) => {
    setInputValue(e.target.value)
  }

  const handleCalculate = () => {
    let customer_1 = parseInt(inputValue) * 12;
    let customer = 0;
    let first_benefit = 0;
    let second_benefit = 0;

    for (let i = 0; i < parseInt(valueFromDurationPeriod); i++) {
      first_benefit += customer * 0.08;
      second_benefit += customer * 0.07;
      customer += customer_1;

      console.log(i)
      console.log(customer, first_benefit, second_benefit)
      console.log(customer + first_benefit + second_benefit)
    }

    setResult(customer + first_benefit + second_benefit);
  }

  const handleValueFromDurationPeriodChange = (e) => {
    setValueFromDurationPeriod(e.target.value);
  }

  return(
    <>
      <div>
        <p>Калькулятор по Bilim-Life</p>
        <div>
          <p>Выберите платеж:</p>
          <input type="radio" id="monthly" name='Pay'/>
          <label htmlFor="monthly">Ежемесячный</label>
          <input type="radio" id="monthly" name='Pay'/>
          <label htmlFor="once">Единовременный</label>
        </div>
        <div>
          <p>Введите сумму ежемесячного платежа:</p>
          <input type='number' value={inputValue} onChange={handleInputChange}/>
        </div>
        <div>
          <p>Введите срок страховки (лет):</p>
          <input type='number' value={valueFromDurationPeriod} onChange={handleValueFromDurationPeriodChange}/>
        </div>
        <button onClick={handleCalculate}>Вычислить</button>
        {
          result !== null && (
            <p>
              Итоговая выплата в учебное заведение: {result} тенге
            </p>
        )}
      </div>
    </>
  );
}

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <img height="160" width="160" src={halykLogo} alt="no img" />
    <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/chatbot" element={<Chatbot />} />
          <Route path="/calculator" element={<Calculator />} />
        </Routes>
    </div>
    <div style={{ position: 'fixed', bottom: 0, left: 0, width: '100%', background: '#f0f0f0', padding: '10px', textAlign: 'center' }}>
          <NavLink to="/" >Home</NavLink>
          <NavLink to="/chatbot">Chatbot</NavLink>
          <NavLink to="/calculator">Calculator</NavLink>
    </div>
    </>
  )
}

export default App;
