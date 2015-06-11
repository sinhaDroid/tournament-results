# Tournament-Results

My solution for the Tournament Results project. Part of Udacity's full stack developer Nanodegree.

This is a python module to manage players, matches and number of matches won in a Swiss Style Tournament.

## Instructions to run project.

1. In terminal, cd Vagrant

2. In terminal, vagrant up. The vagrant virtual machine will start.

3. In terminal, vagrant ssh to login to the virtual machine and cd /vagrant/tournament to go to the shared directory.

4. In the VM, psql to start up postgres.

5. Create a database with CREATE DATABASE tournament;

6. Connect to the tournament database with \c tournament

7. Import the tables and views with \i tournament.sql 

8. Exit postgres with \q

9. Run the tests with python tournament_test.py

10. If all tests pass, everything is good. Import tournament.py into your Python project and build the Swiss Style tournament app of your dreams.


