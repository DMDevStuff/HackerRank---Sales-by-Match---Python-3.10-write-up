##    https://www.hackerrank.com/challenges/sock-merchant/problem

##    There is a large pile of socks that must be paired by color. Given an
##    array of integers representing the color of each sock, determine how
##    many pairs of socks with matching colors there are.

#   changed given variables:
#   n => number_of_socks
#   ar => sock_list

##### ##### ##### #####

#   Iterative solution
#   O(n)
#   n is the length of sock list
#   one pass through sock_list to create sock_occurence_table
#   key:value => color:count
#   one pass through sock_occurence_table to find the number of pairs
#   integer division by 2 will find this
#   for example: if we have 7 socks of a certain color
#   7 // 2 = 3 pairs

def sockMerchant(number_of_socks, sock_list):

    sock_occurrence_table = dict()
    pairs_found = 0

    for sock in sock_list:

        try:
            sock_occurrence_table[sock] += 1

        except:
            sock_occurrence_table[sock] = 1

    for sock_color in sock_occurrence_table:

        pairs_found += sock_occurrence_table[sock_color] // 2

    return pairs_found
