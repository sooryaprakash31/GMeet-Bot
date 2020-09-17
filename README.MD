# GMeet-Bot

## Requirements

- [python3](https://www.python.org/downloads/)
- `pip install requirements.txt`

## Setup

1. `cd GMeet-Bot`
2. Get the Course Names from your classroom
   <img src="docs/images/CourseName.png" align="center" height="150" width="450">

3. Insert the Course Name at the appropriate position in `schedule.csv`</br>
   Example:
   > CS16004-SemC 
   > - Mon - 09:15
   > - Tue - 11:25 
   > - Thu - 14:20
   ></br>
   ><table>
   <th>Day</th>
    <th>09:15</th>
    <th>11:25</th>
    <th>14:20</th>
    <tr>
    <td>Mon</td>
    <td>CS16004-SemC</td>
    <td></td>
    <td></td>
    </tr>
    <tr>
    <td>Tue</td>
    <td></td>
    <td>CS16004-SemC</td>
    <td></td>
    </tr>
    <tr>
    <td>Wed</td>
    <td></td>
    <td></td>
    <td></td>
    </tr>
    <tr>
    <td>Thu</td>
    <td></td>
    <td></td>
    <td>CS16004-SemC</td>
    </tr>
    <tr>
    <td>Fri</td>
    <td></td>
    <td></td>
    <td></td>
    </tr>
   </table>
    
- Repeat this for all the Courses to populate the `schedule.csv` with your schedule
4. Enter your account credentials in `config.ini`</br>
   Example:
   >```
    >[AUTH]
    >USERNAME=username@abc.com
    >PASSWORD=password
   >```
5. Download geckodriver from [here](https://github.com/mozilla/geckodriver/releases) and place it in the folder
6. Create a profile in Firefox and block the camera and microphone access for google meet.
   </br>
   <img src="docs/images/Firefox_permissions.png" aligh="center" height="200" width="390">
   
7. Get the path for the created profile using 
   ```
   about:profiles
   ```
   and include it [here]().

## Execution
1. `cd GMeet-Bot`
2. `python3 class_auto.py`


## Output

- The program will run in the background until class time.
- When the time hits one of the class timings, 
  1. The program automatically fires up the browser.
  2. Logs in your account into google classroom.
  3. Finds the Course from `schedule.csv`.
  4. Joins the meeting using the `Meet Link` in the course room.
  5. After one hour, ends the meeting and closes the browser.