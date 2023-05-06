import json
import requests

class ScreenshotsPagepixels:
  def __init__(self, bearer_token):
    self.base_url = 'https://api.pagepixels.com'
    self.bearer_token = bearer_token
    self.headers = {'Authorization': f'Bearer {self.bearer_token}'}

  def snap(self, options=None):
    return self.get_request('/snap', options)

  def screenshot_configs(self, options=None):
    return self.get_request('/screenshot_configs', options)

  def create_screenshot_config(self, options=None):
    return self.post_request('/screenshot_configs', options)

  def get_screenshot_config(self, id):
    return self.get_request(f'/screenshot_configs/{id}')

  def update_screenshot_config(self, id, options=None):
    return self.patch_request(f'/screenshot_configs/{id}', options)

  def delete_screenshot_config(self, id):
    return self.delete_request(f'/screenshot_configs/{id}')

  def screenshot_config_screenshots(self, id, options=None):
    return self.get_request(f'/screenshot_configs/{id}/screenshots', options)

  def screenshot_config_change_notifications(self, id, options=None):
    return self.get_request(f'/screenshot_configs/{id}/change_notifications', options)

  def job_status(self, job_id):
    return self.get_request(f'/jobs/{job_id}')

  def capture_screenshot(self, id):
    return self.post_request(f'/screenshot_configs/{id}/capture')

  def screenshots(self, options=None):
    return self.get_request('/screenshots', options)

  def change_notifications(self, options=None):
    return self.get_request('/change_notifications', options)

  def get_request(self, path, options=None):
    if options is None:
      options = {}
    response = requests.get(f'{self.base_url}{path}', params=options, headers=self.headers)
    response.raise_for_status()
    return response.json() if path != "/snap" or "json" in options else response.content

  def post_request(self, path, options=None):
    if options is None:
      options = {}
    headers = {**self.headers, 'Content-Type': 'application/json'}
    response = requests.post(f'{self.base_url}{path}', json=options, headers=headers)
    response.raise_for_status()
    return response.json()

  def patch_request(self, path, options=None):
    if options is None:
      options = {}
    headers = {**self.headers, 'Content-Type': 'application/json'}
    response = requests.patch(f'{self.base_url}{path}', json=options, headers=headers)
    response.raise_for_status()
    return response.json()

  def delete_request(self, path):
    response = requests.delete(f'{self.base_url}{path}', headers=self.headers)
    response.raise_for_status()
    return response.json()