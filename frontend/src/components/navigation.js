import React, { useMemo } from 'react'
import { NavLink, useNavigate } from 'react-router-dom';
import 'assets/css/nav.css'
import { USER_DESC } from 'components/contants';
import { navList } from 'components/contants'


function Navigation(props) {
  const navgate = useNavigate()
  const UserDesc = JSON.parse(localStorage.getItem(USER_DESC)) || { username: "Please Login" }

  // Cache the page DOM to avoid multiple renderings and performance congestion
  const links = useMemo(() => navList.map(item => (
    <NavLink
      key={item.key}
      to={item.path}
      className='a'
      activeClassName='active'
      children={item.title}
    />
  )))

  // Click logout
  const logout = () => {
    localStorage.removeItem(USER_DESC)
    navgate('/login', { replace: true })
  }

  return (
    <nav className='topNav'>
      {links}
      <div className='user'>{UserDesc.username}</div>
      <div onClick={logout} className='a' children='logout' />
    </nav>
  )
}

export default Navigation