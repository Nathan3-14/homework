# Tests
| Test Name          | Collisions                            | End                | Lock and Key                                                         | Chests               |
|:------------------:|:-------------------------------------:|:------------------:|:--------------------------------------------------------------------:|:--------------------:|
| Action             | Move into wall                        | Walk to end square | Walk to lock, walk to key, walk to lock                              | Move to chest        |
| Expected results   | Player returns to original position   | Game finishes      | Player cannot move to it, player picks up key, player can move to it | Player collects loot |
| Actual results     | N/A                                   | N/A                | N/A                                                                  | N/A                  |