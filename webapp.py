def execute_query_noncompliant(request):
    import sqlite3
    name = request.GET.get("name")
    # リクエストパラメータから取得した値をそのままSQLに
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    with sqlite3.connect("example.db") as connection:
        cursor = connection.cursor()
        # Noncompliant: user input is used without sanitization.
        cursor.execute(query)
        connection.commit()
        connection.close()

        
        
def exec_command_noncompliant():
    from paramiko import client
    from flask import request
    address = request.args.get("address")
    # リクエストから取得した値をそのままコマンドラインのパラメータに
    cmd = "ping -c 1 %s" % address
    client = client.SSHClient()
    client.connect("ssh.samplehost.com")
    # Noncompliant: address argument is not sanitized.
    client.exec_command(cmd)

    
    
@app.route('/redirect')
def redirect_url_noncompliant():
    from flask import request, redirect
    endpoint = request.args['url']
    # リクエストから取得したパラメータをそのままレスポンスとして返却
    # Noncompliant: redirect to a user-supplied URL without sanitization.
    return redirect(endpoint)
