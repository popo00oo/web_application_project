import { Outlet } from 'react-router-dom'

function Content(props) {
  return (
    <div style={{ padding: '1rem' }}>
      <Outlet />
    </div>
  )
}

export default Content