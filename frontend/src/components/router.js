import { lazy } from 'react'  // Load hook
import { Suspense } from 'react'
import Loading from 'components/loading'


const lazyLoad = component => <Suspense fallback={<Loading />}>{component}</Suspense >

// components import
const Layout = lazy(() => import('components/template'))
const Home = lazy(() => import('components/pages/home'))
const Login = lazy(() => import('components/pages/login'))
const Register = lazy(() => import('components/pages/register'))
const Notice = lazy(() => import('components/pages/notice'))
const Publish = lazy(() => import('components/pages/publish'))
const Lost = lazy(() => import('components/pages/lost'))

// Router table
const appRouter = [
  {
    path: '/',
    element: lazyLoad(<Layout />),
    children: [
      {
        index: true,
        element: lazyLoad(<Home />)
      },
      {
        path: '/notice',
        element: lazyLoad(<Notice />)
      },
      {
        path: '/publish',
        element: lazyLoad(<Publish />)
      },
      {
        path: '/lost',
        element: lazyLoad(<Lost />)
      },
    ]
  },
  {
    path: '/login',
    element: lazyLoad(<Login />),
  },
  {
    path: '/register',
    element: lazyLoad(<Register />),
  },
  {
    path: '*',
    element: lazyLoad(<>DIDN'T FIND YOUR PAGE</>) // 404 page，
  }
]

export default appRouter