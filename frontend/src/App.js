import { useRoutes } from 'react-router-dom'
import routers from 'components/router'

function App() {
  // Using route，render the page according to the configuration of the routing table
  const element = useRoutes(routers)
  return (
    <>
      {element}
    </>
  );
}

export default App;
