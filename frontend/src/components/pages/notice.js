import React, { useState, useEffect, useMemo } from 'react'
import { getNotice, deleteNotice } from 'components/network/api'
import { getUserDesc } from 'components/utils'
import st from 'assets/css/notice.module.css'

function Notice(props) {
  const userDesc = getUserDesc()
  const [params, setparams] = useState({ page: 1 })
  const [dataList, setdataList] = useState([])

  useEffect(() => {
    getData()
  }, [params])

  const getData = () => {
    getNotice(params).then(res => {
      setdataList(res.data.results)
    }).catch(err => console.log(err))
  }

  const delRow = roeId => {
    deleteNotice(roeId).then(res => {
      if (res.status) {
        setdataList(dataList.filter(item => item.id !== roeId))
      }
    }).catch(err => console.log(err))
  }

  const dataDom = useMemo(() => {
    return dataList.map(item => {
      return <div key={item.id} className={st.row}>
        <div className={st.content}>{item.content}</div>
        <div className={st.timer}>{item.create_time}</div>
        <div className={st.timer}>{item.update_time}</div>
        <button className={`${st.delBtn} ${item.user !== userDesc.id ? st.disabled : ''}`} onClick={() => delRow(item.id)} disabled={item.user !== userDesc.id}>delete</button>
      </div>
    })
  }, [dataList])

  return (
    <>
      <div className={`${st.row} ${st.title}`}>
        <div className={st.content}>Content</div>
        <div className={st.timer}>Create_time</div>
        <div className={st.timer}>Update_time</div>
        <div>Options</div>
      </div>
      {
        dataDom
      }
    </>
  )
}

export default Notice