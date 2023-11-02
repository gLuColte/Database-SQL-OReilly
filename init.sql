USE master;
GO

-- Create a new login
CREATE LOGIN [developer001] WITH PASSWORD = 'developer001password!';
GO

-- Create a user for the login
CREATE USER [developer001] FOR LOGIN [developer001];
GO

-- Add the user to the sysadmin role
ALTER SERVER ROLE [sysadmin] ADD MEMBER [developer001];
GO

-- Create a new database called "development"
CREATE DATABASE [development];
GO