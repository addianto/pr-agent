from unittest.mock import patch

from fastapi import FastAPI

from pr_agent.servers import start_server, DEFAULT_HOST, DEFAULT_PORT


class TestStartServer:

    @patch('pr_agent.servers.get_settings')
    @patch('pr_agent.servers.uvicorn.run')
    def test_start_server(self, mock_uvicorn_run, mock_get_settings):
        # Arrange
        app = FastAPI()
        mock_settings = {
            "config.host": "127.0.0.1",
            "config.port": 8000
        }
        mock_get_settings.return_value = mock_settings

        # Act
        start_server(app)

        # Assert
        assert mock_get_settings.call_count == 2
        mock_uvicorn_run.assert_called_once_with(app, host="127.0.0.1", port=8000)

    @patch('pr_agent.servers.get_settings')
    @patch('pr_agent.servers.uvicorn.run')
    @patch.dict('os.environ', {'PORT': '9000'})
    def test_start_server_with_env_port(self, mock_uvicorn_run, mock_get_settings):
        # Arrange
        app = FastAPI()
        mock_settings = {
            "config.host": "127.0.0.1",
            "config.port": 8000
        }
        mock_get_settings.return_value = mock_settings

        # Act
        start_server(app)

        # Assert
        assert mock_get_settings.call_count == 2
        mock_uvicorn_run.assert_called_once_with(app, host="127.0.0.1", port=9000)

    @patch('pr_agent.servers.get_settings')
    @patch('pr_agent.servers.uvicorn.run')
    def test_start_server_with_defaults(self, mock_uvicorn_run, mock_get_settings):
        # Arrange
        app = FastAPI()
        mock_settings = {}
        mock_get_settings.return_value = mock_settings

        # Act
        start_server(app)

        # Assert
        assert mock_get_settings.call_count == 2
        mock_uvicorn_run.assert_called_once_with(app, host=DEFAULT_HOST, port=DEFAULT_PORT)
