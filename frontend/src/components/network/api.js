// Get all api
import fetch from './request'

// user
export const login = data => fetch.post('/auth/login', data)
export const register = data => fetch.post('/auth/register', data)

// notice
export const getNotice = params => fetch.get('/service/notice', params)
export const postNotice = data => fetch.post('/service/notice', data)
export const patchNotice = data => fetch.patch('/service/notice', data)
export const deleteNotice = id => fetch.delete('/service/notice', { id })

// lost
export const getLost = params => fetch.get('/service/lost', params)
