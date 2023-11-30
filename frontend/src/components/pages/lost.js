import React, { useEffect, useState, useMemo } from 'react'
import { getLost } from 'components/network/api'
import st from 'assets/css/lost.module.css'

function Lost(props) {
  const [params, setParams] = useState()
  const [searchData, setSearchData] = useState('')
  const [dataList, setDataList] = useState([])

  useEffect(() => {
    getData(params)
  }, [params])

  // request data
  const getData = params => {
    getLost(params).then(res => {
      setDataList(res.data.results)
    }).catch(err => console.log(err))
  }


  const onChange = e => {
    setSearchData(e.target.value)
  }

  // search
  const searchClick = () => {
    setParams({ category__icontains: searchData })
  }

  // 重置搜索
  const reset = () => {
    setParams({})
    setSearchData('')
  }

  // Cache page content
  const dataDom = useMemo(() => {
    return dataList.map(item => {
      return <div key={item.id} className={st.row}>
        <div className={st.item}>{item.location}</div>
        <div className={st.item}>{item.date}</div>
        <div className={st.item}>{item.category}</div>
        <div className={st.item}>{item.upass}</div>
        <div className={st.item}>{item.desc}</div>
        <div className={st.item}>{item.create_time}</div>
        <div className={st.item}>{item.update_time}</div>
      </div>
    })
  }, [dataList])

  return (
    <div className={st.box}>
      <div className={st.search}>
        <input maxLength={30} className={st.input} onChange={onChange} type="text" value={searchData} placeholder='search category' />
        <button className={st.btn} onClick={searchClick}>search</button>
        <button className={st.btn} onClick={reset}>Reset</button>
      </div>
      <div className={`${st.row} ${st.title}`}>
        <div className={st.item}>location</div>
        <div className={st.item}>date</div>
        <div className={st.item}>category</div>
        <div className={st.item}>upass</div>
        <div className={st.item}>desc</div>
        <div className={st.item}>create_time</div>
        <div className={st.item}>update_time</div>
      </div>
      {dataDom}
    </div>
  )
}

export default Lost