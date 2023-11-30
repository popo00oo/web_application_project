import React, { useState } from 'react'
import { postNotice } from 'components/network/api'
import st from 'assets/css/publish.module.css'

function Publist(props) {
  // input
  const [text, settext] = useState('')
  // submit
  const submit = () => {
    if (text.length === 0) {
      return alert('Please enter the details of the lost item')
    }
    postNotice({ content: text }).then(res => {
      if (res.status) {
        alert(res.info)
        settext('')
      }
    }).catch(err => console.log(err))
  }

  const onChange = (e) => {
    settext(e.target.value)
  }

  return (
    <div className={st.box}>
      <textarea value={text} maxLength={200} onChange={onChange} className={st.input} cols="30" rows="10" placeholder='Please enter the details of the lost item' />
      <button onClick={submit} className={st.btn}>publish</button>
    </div>
  )
}

export default Publist