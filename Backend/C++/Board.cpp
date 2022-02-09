#include <iostream>
#include "Board.h"

using namespace std;

// Creates an empty 10x10 board of water
//INitializer list
// idNum in parameter as an alternative to a setter
Board::Board(int idNum) : m_rows(10), m_cols(10), shipOrientation(0), id(idNum)
{
	//	int m_start_row, m_end_row;
	//	int m_start_col, m_end_col;
	//	int totalShips = 1;


	m_board = new char *[m_rows];
	for (int i = 0; i < m_rows; i++)
	{
		m_board[i] = new char[m_cols];
	}
	for (int i = 0; i < m_rows; i++)
	{
		for (int j = 0; j < m_cols; j++)
		{
			m_board[i][j] = '.';
		}
	}
}

Board::~Board()
{
	for (int i = 0; i < m_rows; i++)
	{
		delete[] m_board[i];
	}
	delete[] m_board;
}

void Board::placeShip(int i, int j, int length, int orientation)
{
	m_board[i][j] = 'S';
	int iPos = i;
	int jPos = j;
	shipOrientation = orientation;

	// If ship oriented up
	if (shipOrientation == 1)
	{
		int shipSize = length;
		while (shipSize != 1)
		{
			m_board[iPos - 1][jPos] = 'S';
			shipSize--;
			iPos--;
		}
	}
	// If ship oriented down
	if (shipOrientation == 2)
	{
		int shipSize = length;
		while (shipSize != 1)
		{
			m_board[iPos + 1][jPos] = 'S';
			shipSize--;
			iPos++;
		}
	}
	// If ship oriented left
	if (shipOrientation == 3)
	{
		int shipSize = length;
		while (shipSize != 1)
		{
			m_board[iPos][jPos - 1] = 'S';
			shipSize--;
			jPos--;
		}
	}
	// If ship oriented right
	if (shipOrientation == 4)
	{
		int shipSize = length;
		while (shipSize != 1)
		{
			m_board[iPos][jPos + 1] = 'S';
			shipSize--;
			jPos++;
		}
	}
}

bool Board::validShipPosition(int i, int j, int length, int orientation)
{
	/*if ((i > 0 && i < 11) && (j > 0 && j < 11))
	{
		if (m_board[i][j] == '.')
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	if (orientation == 1)
	{
		for (int row = 1; row <= length; row++)
		{
			validShipPosition(i, )
		}
	}*/
}

bool Board::allShipsSunk()
{
	for (int i = 0; i < m_rows; i++)
	{
		for (int j = 0; j < m_cols; j++)
		{
			if (m_board[i][j] == 'S')
			{
				return false;
			}
		}
	}

	return true;
}

bool Board::updateBoardHit(int i, int j)
{
	if (m_board[i][j] == '.')
	{
		m_board[i][j] = 'M';
		return false;
	}

	else if (m_board[i][j] == 'S')
	{
		m_board[i][j] = 'X';
		return true;
	}
}
// invoked after ship is hit
bool Board::shipDestroyed(int i, int j)
{
	 
	if (i == 0 && j == 0)
	{
		if (m_board[i + 1][j] != 'S' && m_board[i][j + 1] != 'S')
		{
			return true;
		}
		return false;
	}

	else if (i == 0 && j == 9)
	{
		if (m_board[i + 1][j] != 'S' && m_board[i][j - 1] != 'S')
		{
			return true;
		}
		return false;
	}

	else if (i == 9 && j == 0)
	{
		if (m_board[i][j + 1] != 'S' && m_board[i - 1][j] != 'S')
		{
			return true;
		}
		return false;
	}

	else if (i == 9 && j == 9)
	{
		if (m_board[i][j - 1] != 'S' && m_board[i - 1][j] != 'S')
		{
			return true;
		}
		return false;
	}

	else if (i == 0)
	{
		if (m_board[i + 1][j] != 'S' && m_board[i][j + 1] != 'S' && m_board[i][j - 1] != 'S')
		{
			return true;
		}
		return false;
	}

	else if (i == 9)
	{
		if (m_board[i - 1][j] != 'S' && m_board[i][j + 1] != 'S' && m_board[i][j - 1] != 'S')
		{
			return true;
		}
		return false;
	}

	else if (j == 0)
	{
		if (m_board[i - 1][j] != 'S' && m_board[i][j + 1] != 'S' && m_board[i + 1][j] != 'S')
		{
			return true;
		}
		return false;
	}

	else if (j == 9)
	{
		if (m_board[i - 1][j] != 'S' && m_board[i][j - 1] != 'S' && m_board[i + 1][j] != 'S')
		{
			return true;
		}
		return false;
	}

	else if (m_board[i + 1][j] != 'S' && m_board[i][j + 1] != 'S' && m_board[i - 1][j] != 'S' && m_board[i][j - 1] != 'S') // D R U L
	{
		return true;
	}

	else
	{
		return false;
	}
}

/*void Board::printBoardWOShip()
{
	for (int i = 0; i < m_rows; i++)
	{
		for (int j = 0; j < m_cols; j++)
		{
			if (m_board[i][j] == 'S')
			{
				cout << '.';
			}

			else
			{
				cout << m_board[i][j];
			}
		}
		cout << endl;
	}
	cout << endl;
}

void Board::printBoardWShip()
{
	for (int i = 0; i < m_rows; i++)
	{
		for (int j = 0; j < m_cols; j++)
		{
			cout << m_board[i][j];
		}
		cout << endl;
	}
	cout << endl;
}*/


void Board::printBoardWOShip()
{
    int row = 01;
    cout << "   A B C D E F G H I J\n";
    for (int i = 0; i < m_rows; i++)
    {
        if (row != 10)
        {
            cout << ' ' << row << ' ';
            row++;
        }
        else
        {
            cout << row << ' ';
        }
        for (int j = 0; j < m_cols; j++)
        {
            if (m_board[i][j] == 'S')
            {
                cout << ". ";
            }
            else
            {
                cout << m_board[i][j] << ' ';
            }
        }
        cout << endl;
    }
	cout << endl;
}

void Board::printBoardWShip()
{
    int row = 01;
    cout << "   A B C D E F G H I J\n";
    for (int i = 0; i < m_rows; i++)
    {
        if (row != 10)
        {
            cout << ' ' << row << ' ';
            row++;
        }
        else
        {
            cout << row << ' ';
        }
        for (int j = 0; j < m_cols; j++)
        {
            cout << m_board[i][j] << ' ';
        }
        cout << endl;
    }
	cout << endl;
}
