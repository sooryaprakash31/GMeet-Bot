# GMeet-Bot

## Requirements

- [python3](https://www.python.org/downloads/)
- Clone of this repository
- Firefox browser
- `pip install requirements.txt`

## Setup

1. `cd GMeet-Bot`
2. Enter your account credentials in `config.ini`</br>
   Example:
   >```
    >[AUTH]
    >USERNAME=username@abc.com
    >PASSWORD=password
   >```
3. Download geckodriver from [here](https://github.com/mozilla/geckodriver/releases) and place it in the folder
4.  Create a profile in Firefox and block the camera and microphone access for google meet.  
   <img src="docs/images/Firefox_permissions.png" align="center" >
   
5. Get the path for the created profile using 
   ```
   about:profiles
   ```
   and include it [here]().
6. Get the Course Names from your classroom  
   <img src="docs/images/CourseName.png" align="center">

7. Insert the Course Name at the appropriate position in `schedule.csv`</br>
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

## Customization

1. Class Timings
   - Modify the class timings in [source code]() as well as `schedule.csv`
   - Use 24-hour time format
2. This program is set to run for three classes per day. Modify it here by changing 2 here to 'n'-1 for 'n' classes.
   ```
   if self.count < 2:
        self.count = self.count + 1
   ```

## Troubleshooting
1. Google account must not be already logged in.
2. `schedule.csv` must contain the exact course names.
3. Slow internet connection may cause program to crash.

# Leave a  if you find this useful.