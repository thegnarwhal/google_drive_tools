import pytest

from count_files_and_folders import count_files_and_folders_recursive

@pytest.mark.parametrize("folder_id, expected_file_count, expected_folder_count", [
    ("1WnwiNw3Zt9-ArXS6BYTxOkTV1TRvwUmQ", 5, 10),
])

def test_count_files_and_folders(drive, folder_id, expected_file_count, expected_folder_count):
    """Test the count filed and folders function"""

    file_count, folder_count = test_count_files_and_folders(drive, folder_id)

    assert file_count == expected_file_count
    assert folder_count == expected_folder_count