class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:  # Main function; takes nums and returns sorted nums

        def merge(arr, L, M, R):  # Merge two already-sorted halves: [L...M] and [M+1...R]
            left, right = arr[L:M+1], arr[M+1:R+1]  # Copy the left and right halves into separate lists
            i, j, k = L, 0, 0  # i = position in original array; j = position in left; k = position in right

            while j < len(left) and k < len(right):  # Continue while both halves still have elements
                if left[j] <= right[k]:  # If current left element is smaller/equal
                    arr[i] = left[j]  # Put the left element into the original array
                    j += 1  # Move to the next element in left
                else:  # Otherwise, the right element is smaller
                    arr[i] = right[k]  # Put the right element into the original array
                    k += 1  # Move to the next element in right
                i += 1  # Move to the next position in the original array

            while j < len(left):  # If elements remain in the left half
                arr[i] = left[j]  # Copy the remaining left element into the original array
                j += 1  # Move to the next left element
                i += 1  # Move to the next position in the original array

            while k < len(right):  # If elements remain in the right half
                arr[i] = right[k]  # Copy the remaining right element into the original array
                k += 1  # Move to the next right element
                i += 1  # Move to the next position in the original array

        def mergesort(arr, l, r):  # Recursively sorts the portion of arr from index l to index r
            if l == r:  # If the portion contains only one element
                return arr  # A single element is already sorted

            m = (l + r) // 2  # Find the middle index

            mergesort(arr, l, m)  # Recursively sort the left half
            mergesort(arr, m + 1, r)  # Recursively sort the right half

            merge(arr, l, m, r)  # Merge the two sorted halves together
            return arr  # Return the sorted array

        return mergesort(nums, 0, len(nums) - 1)  # Sort the entire array and return it