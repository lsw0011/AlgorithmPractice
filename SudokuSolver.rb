require 'pry'
@count = 0
def getRow(ind)
  return ind/9
end

def getColumn(ind)
  return ind%9
end

def getGrid(ind)
  y = ind/27
  x = ind%9
  #returns grid offset
  return xCheck(x) + yCheck(y)
end

def yCheck(num)
  if num == 0
    return 0
  elsif num == 1
    return 3
  else
    return 6
  end
end

def xCheck(num)
  if num < 3
    return 0
  elsif num < 6
    return 1
  else num < 9
    return 2
  end
end

def rowValues?(ind, puzzle)
  row_num = getRow(ind)
  row_values = []
  puzzle.each_with_index do |cell, cellNumber|
    if getRow(cellNumber) == row_num
      row_values.push(cell)
    end
  end
  return row_values
end

def columnValues?(ind, puzzle)
  column_num = getColumn(ind)
  column_values = []
  puzzle.each_with_index do |cell, cellNumber|
    if getColumn(cellNumber) == column_num
      column_values.push(cell)
    end
  end
  return column_values
end

def gridValues?(ind, puzzle)
  grid_num = getGrid(ind)
  grid_values = []
  puzzle.each_with_index do |cell, cellNumber|
    if getGrid(cellNumber) == grid_num
      grid_values.push(cell)
    end
  end
  return grid_values
end

def blank?(cell)
  cell == '-' ? true : false
end

def board(string)
  puzzle = string.chars
end

def cellPossValues(ind, puzzle)
  poss_values = ('1'..'9').to_a - gridValues?(ind, puzzle) - columnValues?(ind, puzzle) - rowValues?(ind, puzzle)
end

def lengthOne?(array)
  array.length == 1? true : false
end

def boardComplete?(puzzle)
  full = ('1'..'9').to_a
  puzzle.each_index do |cellNumber|
    if !(rowValues?(cellNumber, puzzle).sort == full && columnValues?(cellNumber, puzzle).sort == full && gridValues?(cellNumber, puzzle).sort == full)
      return false
    end
  end
  return true
end

def removeBlanks(array)
  array.delete_if{|element| element == "-"}
end

def noDuplicates?(array)
  noBlanks = removeBlanks(array)
  noBlanks.uniq == noBlanks ? true : false
end

def isValid?(puzzle)
  if possValues.length == 0
    return false
  end
  puzzle.each_index do |cellNum|
    if !noDuplicates?(rowValues?(cellNum, puzzle)) || !noDuplicates?(columnValues?(cellNum, puzzle)) || !noDuplicates?(gridValues?(cellNum, puzzle))
      return false
    end
  end
  return true
end
# def solve(string)
#   puzzle = board(string)
#   solvable = true

#   while solvable == true
#     flag = false
#       puzzle.each_with_index do |cell, cellNumber|
#         possValues = cellPossValues(cellNumber, puzzle)
#         if blank?(cell) && lengthOne?(possValues)
#           puzzle[cellNumber] = possValues[0]
#           flag = true
#         end
#       end

#     if flag == false && !boardComplete?(puzzle)
#       initialstate = puzzle.dup
#       return guessSolve(puzzle, initialstate)
#       break
#     end
#   end
# end

def getBlank(puzzle)
  puzzle.each_with_index do |cell, cellNum|
    if cell == "-"
      return cellNum
    end
  end
end

def recursive_solve(board, initialstate)
  @count += 1
  firstBlank = getBlank(board)
  possValues = cellPossValues(firstBlank, board)
  if possValues.length == 0
    return nil
  end
  possValues.each do |value|
    board[firstBlank] = value
    if boardComplete?(board)
      return board
    else
      check = recursive_solve(board, initialstate)
      if check == nil
        revert(firstBlank, board, initialstate)
      elsif boardComplete?(board)
        return board
      end
    end
  end
  return nil
end


def returnedValueComplete(returnedvalue)
  begin
    if boardComplete?(returnedvalue)
      return true
    end
  rescue

  ensure
    return false
  end
end

def revert(firstBlank, puzzle, initialstate)
  puzzle.each_with_index do |value, index|
    if index > firstBlank
      puzzle[index] = initialstate[index]
    end
  end
end

board = "1-58-2----9--764-52--4--819-19--73-6762-83-9-----61-5---76---3-43--2-5-16--3-89--"
finalboard = board(board)
initialstate = finalboard.dup

p recursive_solve(finalboard, initialstate)

