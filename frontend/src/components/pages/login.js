import { useNavigate, Link } from 'react-router-dom'
import React, { useState } from 'react'
import { login } from 'components/network/api'
import { USER_DESC } from 'components/contants'
import st from 'assets/css/login.module.css'

function Login(props) {
  const navigate = useNavigate()

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  // two input
  const inputChange = (e, isUsername) => {
    if (isUsername) {
      setUsername(e.target.value)
    } else {
      setPassword(e.target.value)
    }
  }

  // rest input
  const reset = () => {
    setUsername('')
    setPassword('')
  }

  // click login
  const submit = () => {
    login({ username, password }).then(res => {
      if (res.status) {

        localStorage.setItem(USER_DESC, JSON.stringify(res.data))
        // redirect to main page
        navigate('/')
      } else {
        reset()
        window.alert(res.errs)
      }
    }).catch(err => console.log(err))
  }

  return (
    <div className={st.box}>
      <div className={st.content}>
        <h2>Login</h2>
        <input className={st.inputText} type="text" value={username} onChange={e => inputChange(e, true)} placeholder='Username' />
        <input className={st.inputText} type="password" value={password} onChange={e => inputChange(e, false)} placeholder='Password' />
        <button className={st.btn} onClick={submit}>Login</button>
        <div><Link to='/register' children='click me to register' /> OR <a target="_blank" rel="noreferrer" href="http://localhost:8000/admin">admin login</a></div>
      </div>
    </div>
  )
}

export default Login