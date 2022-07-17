"""
Print diamond
         *
        * *
       * * *
      * * * *
     * * * * *
    * * * * * *
   * * * * * * *
  * * * * * * * *
 * * * * * * * * *
* * * * * * * * * *
"""

total = int(input("Enter the number of rows: "))


def print_line(spaces: int, nb_stars: int):
    for i in range(spaces):
        print(' ', end='')
    for nb_star in range(nb_stars):
        print('* ', end='')
    print('')  # print return caret


# Main
for idx in range(total):
    print_line(spaces=total - idx - 1, nb_stars=idx + 1)
