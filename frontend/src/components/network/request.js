// Encapsulate fetch for easy of use.
import { getUserDesc } from 'components/utils'

// API address
const baseUrl = 'http://localhost:8000'

// fetch client
class FetchClient {
  constructor() {
    this.get = this.get.bind(this);
    this.post = this.post.bind(this);
    this.patch = this.patch.bind(this);
    this.put = this.put.bind(this);
    this.delete = this.delete.bind(this);
  }

  get(url, data) {
    return this.request(url, 'GET', data);
  }

  post(url, data) {
    return this.request(url, 'POST', data);
  }

  patch(url, data) {
    return this.request(url, 'PATCH', data);
  }

  put(url, data) {
    return this.request(url, 'PUT', data);
  }
  delete(url, data) {
    return this.request(url, 'DELETE', data);
  }

  request(url, method, data) {
    url = `${baseUrl}${url}`;
    let body = JSON.stringify(data);
    if (method === 'GET') {
      url = `${url}?${new URLSearchParams(data).toString()}`;
      body = null;
    }
    return new Promise((resolve, reject) => {
      fetch(url, { method, headers: { 'Content-Type': 'application/json;charset=utf-8', 'Authorization': getUserDesc().token }, body })
        .then(response => {
          if (!response.ok) {
            if (response.status === 403) {
              // localStorage.removeItem(USER_DESC);
              window.location.href = '/#/login';
            }
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          resolve(data);
        })
        .catch(error => {
          reject(error);
        });
    });
  }
}

const fetchClient = new FetchClient();
export default fetchClient;
