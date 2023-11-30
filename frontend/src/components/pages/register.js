import { useNavigate, Link } from 'react-router-dom'
import React, { useState } from 'react'
import { register } from 'components/network/api'
import st from 'assets/css/login.module.css'
//The user register page, similar to the Login page, can be combined into a single hook
function Register(props) {
  const navigate = useNavigate()
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const inputChange = (e, isUsername) => {
    if (isUsername) {
      setUsername(e.target.value)
    } else {
      setPassword(e.target.value)
    }
  }

  const reset = () => {
    setUsername('')
    setPassword('')
  }
  // submit register
  const submit = () => {
    register({ username, password }).then(res => {

      if (res.status) {
        // 跳转到登陆页面
        navigate('/login')
      } else {
        reset()
        window.alert('Try again please!')
      }
    }).catch(err => console.log(err))
  }

  return (
    <div className={st.box}>
      <div className={st.content}>
        <h2>Register</h2>
        <input className={st.inputText} type="text" value={username} onChange={e => inputChange(e, true)} placeholder='Username' />
        <input className={st.inputText} type="password" value={password} onChange={e => inputChange(e, false)} placeholder='Password' />
        <button className={st.btn} onClick={submit}>Submit</button>
        <div><Link to='/login' children='click me to login' /> OR <a target="_blank" rel="noreferrer" href="http://localhost:8000/admin">admin login</a></div>
      </div>
    </div>
  )
}

export default Register