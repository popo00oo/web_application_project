import { USER_DESC } from 'components/contants'

const user_desc = { id: 0, username: 'not login', token: '' }

// Get user information, set user information to local persistent storage when the user logs in
export function getUserDesc() {
  return JSON.parse(localStorage.getItem(USER_DESC)) || user_desc
}