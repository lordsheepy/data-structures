#!/usr/bin/env python


def quick_sort(unsorted, method='median'):
    if len(unsorted) < 2:
        return unsorted

    piv = pivot(unsorted, method=method)

    lesser = [i for i in unsorted if i < piv]
    greater = [i for i in unsorted if i > piv]
    piv_list = [i for i in unsorted if i == piv]

    less = quick_sort(lesser, method=method)
    great = quick_sort(greater, method=method)

    less.extend(piv_list)
    less.extend(great)
    return less


def pivot(list_inp, method='median'):
    """Defines a pivot point for quicksort, method can be ['first', 'last',
    'median']"""
    if method.lower() == 'median':
        med_list = []
        med_list.append(list_inp[0])
        med_list.append(list_inp[-1])
        med_list.append(list_inp[len(list_inp) // 2])
        med_list.remove(max(med_list))
        med_list.remove(min(med_list))
        return med_list[0]

    if method.lower() == 'first':
        return list_inp[0]

    if method.lower() == 'last':
        return list_inp[-1]

if __name__ == '__main__':
    pass