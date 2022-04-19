# Import libraries
from sshtunnel import SSHTunnelForwarder
import pymysql

# SSH (ec2_public_dns, ec2_user, pem_path, remote_bind_address=(rds_instance_access_point, port))
with SSHTunnelForwarder(('ec2-15-164-145-40.ap-northeast-2.compute.amazonaws.com'), ssh_username="ec2-user",
                        ssh_pkey="./webserver-mk-bit.pem", remote_bind_address=(
        'database-1.cauljkk9souc.ap-northeast-2.rds.amazonaws.com', 3306)) as tunnel:
    print("****SSH Tunnel Established****")

    db = pymysql.connect(
        host='127.0.0.1', user="admin", password="drsong12#",
        port=tunnel.local_bind_port, database="rebit"
    )
    # Run sample query in the database to validate connection
    try:
        # Print all the databases
        with db.cursor() as cur:
            # Print all the tables from the database
            cur.execute('SHOW TABLES FROM rebit')
            for r in cur:
                print(r)

            # Print all the data from the table
            # cur.execute('SELECT * FROM rebit.review')
            cur.execute('INSERT INTO rebit.review (user_id) values ("test3333")')
            for r in cur:
                print(r)
    finally:
        db.commit()
        db.close()

print("YAYY!!")