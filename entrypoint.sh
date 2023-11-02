#!/bin/sh
USERNAME="SA"
PASSWORD="admin123!"

# Start the SQL Server process in the background
/opt/mssql/bin/sqlservr &

# Function to check if SQL Server is ready
is_sql_server_ready() {
  /opt/mssql-tools/bin/sqlcmd -S tcp:localhost,1433 -U "$USERNAME" -P "$PASSWORD" -Q "SELECT 1" &> /dev/null
  return $?
}

# Initial delay before checking if SQL Server is up
echo "Waiting a bit for SQL Server to start..."
sleep 10s

# Wait for SQL Server to come up (max 60 seconds)
i=1
while [ $i -le 12 ]; do
  echo "Checking if SQL Server is ready (Attempt: $i)..."
  if is_sql_server_ready; then
    echo "SQL Server is up - running init.sql"
    # Run the setup script to create the DB
    /opt/mssql-tools/bin/sqlcmd -S tcp:localhost,1433 -U "$USERNAME" -P "$PASSWORD" -i /usr/src/app/init.sql
    if [ $? -eq 0 ]; then
      echo "init.sql executed successfully"
    else
      echo "Failed to execute init.sql"
      cat /usr/src/app/init.sql
      exit 1
    fi
    break
  else
    echo "SQL Server is not ready yet..."
  fi
  sleep 5
  i=$((i+1))
done

if [ $i -gt 12 ]; then
  echo "SQL Server never became ready, exiting..."
  exit 1
fi

echo "Initialization complete. SQL Server is ready for use."

# Wait for the SQL Server process to finish
wait $sql_pid