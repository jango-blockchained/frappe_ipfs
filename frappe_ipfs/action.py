import ipfshttpclient


def upload_file_to_ipfs(file_path="./example.txt"):
    client = ipfshttpclient.connect(
        '/ip4/127.0.0.1/tcp/5001')  # Connect to the IPFS daemon
    res = client.add(file_path)  # Upload the file to IPFS
    ipfs_hash = res['Hash']  # Get the IPFS hash of the uploaded file
    return ipfs_hash
