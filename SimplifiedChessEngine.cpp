
#include <bits/stdc++.h>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long lli;
int current = 1;
int original = 0;

int queen = 1;
int rook = 2;
int bishop = 3;
int knight = 4;
int N = 0;
int NE = 1;
int E = 2;
int SE = 3;
int S = 4;
int SW = 5;
int W = 6;
int NW = 7;

int directions[8] = {4, 5, 1, -3, -4, -5, -1, 3};
int knightDir[8] = {7, 9, 6, -2, -7, -9, -6, 2};

int white = 1;
int black = 0;

int validMove(int position, int direction){
	switch(direction) {
		case 0: return (position / 4 != 3);
		case 1: return (position / 4 != 3 && position % 4 != 3);
		case 2: return (position % 4 != 3);
		case 3: return (position / 4 != 0 && position % 4 != 3);
		case 4: return (position / 4 != 0);
		case 5: return (position / 4 != 0 && position % 4 != 0);
		case 6: return (position % 4 != 0);
		case 7: return (position / 4 != 3 && position % 4 !=0);
	}
}

int validKnightMove(int position, int direction){
	switch(direction) {
		case 0: return (position / 4 <= 1 && position % 4 >= 1);
		case 1: return (position / 4 <= 1 && position % 4 <= 2);
		case 2: return (position / 4 <= 2 && position % 4 <= 1);
		case 3: return (position / 4 >= 1 && position % 4 <= 1);
		case 4: return (position / 4 >= 2 && position % 4 <= 2);
		case 5: return (position / 4 >= 2 && position % 4 >= 1);
		case 6: return (position / 4 >= 1 && position % 4 >= 2);
		case 7: return (position / 4 <= 2 && position % 4 >= 2);

	}
}

int doesCapture(int piecePos, int enemyPieces[][2], int eLength){
	for(int piece = 0; piece < eLength; piece++){
		if(enemyPieces[piece][1] == piecePos){
			return piece;
		}
	}
	return -1;
}

void placePiece(char k, char c, char r, int pieceArray[][2], int pieceIndex){
	int pieceInt;
	int column = c - 'A';
	int row = r - '0' - 1;
	switch(k) {
		case 'Q': pieceInt = queen; break;
		case 'R': pieceInt = rook; break;
		case 'B': pieceInt = bishop; break;
		case 'N': pieceInt = knight; break;
	}
	int piece[2] = {pieceInt, column+row*4};
	copy(piece, piece + 2, pieceArray[pieceIndex]);
}

int notOccupied(int position, int pieces[][2], int length){
	for(int i = 0; i < length; i++){
		if(position == pieces[i][1]){
			return 0;
		}
	}
	return 1;
}

void moves(int position, int kind, vector<int> * moves, int allies[][2], int aLength, int enemies[][2], int eLength){
	int (*pAllies)[2] = allies;
	int (*pEnemies)[2] = enemies;
	if(kind != 4){
		for(int i = 0; i < 8; i++){
			if(kind == 2 && i % 2) continue;
			if(kind == 3 && !(i % 2)) continue;
			int newPosition = position;
			while(validMove(newPosition, i)){
				newPosition += directions[i];
				if(notOccupied(newPosition, pAllies, aLength)){
					moves->push_back(newPosition);
					if(!notOccupied(newPosition, pEnemies, eLength)){
						break;
					}
				}else{
					break;
				}
			}
		}
	}else{
		for(int i = 0; i < 8; i++){
			int newPosition = position;
			if(validKnightMove(newPosition, i)){
				newPosition += knightDir[i];
				if(notOccupied(newPosition, pAllies, aLength)){
					moves->push_back(newPosition);
				}

			}
		}
	}
}

int noBlackQueen(int (*blackPieces)[2], int bLength){
	for(int piece = 0; piece < bLength; piece++){
		if(blackPieces[piece][0] == 1){
			return 0;
		}
	}
	return 1;
}
int noWhiteQueen(int (*whitePieces)[2], int wLength){
	for(int piece = 0; piece < wLength; piece++){
		if(whitePieces[piece][0] == 1){
			return 0;
		}
	}
	return 1;
}

void copyArray(int arr[][2], int arr2[][2], int arrLen){
	for(int i = 0; i < arrLen; i++){
		arr2[i][0] = arr[i][0];
		arr2[i][1] = arr[i][1];
	}
}

int solve(int m, int mLimit, int (*whitePieces)[2], int wLength, int (*blackPieces)[2], int bLength){
	if(noBlackQueen(blackPieces, bLength)){
		return 1;
	}else if(noWhiteQueen(whitePieces, wLength)){
		return 0;
	}else if(m > mLimit){
		return 0;
	}else if(m % 2 == 1){

		for(int piece = 0; piece < wLength; piece++){
			vector<int> possibleMoves;
			moves(whitePieces[piece][1], whitePieces[piece][0], &possibleMoves, whitePieces, wLength, blackPieces, bLength);
			for(int move = 0; move < possibleMoves.size(); move++){
				int newWhitePieces[wLength][2];
				copyArray(whitePieces, newWhitePieces, wLength);
				int capture = doesCapture(possibleMoves[move], blackPieces, bLength);
				if(capture == -1){
					int newBlackPieces[bLength][2];
					copyArray(blackPieces, newBlackPieces, bLength);
					newWhitePieces[piece][1] = possibleMoves[move];
					if(solve(m + 1, mLimit, newWhitePieces, wLength, newBlackPieces, bLength)){
						return 1;
					}else{
						continue;
					}
				}else{
					if(bLength - 1 == 0){
						return 1;
					}
					int newBlackPieces[bLength-1][2];
					int skip = 0;
					for(int bPiece = 0; bPiece < bLength; bPiece++){
						if(bPiece == capture){
							continue;
						}else{
							newBlackPieces[skip][0] = blackPieces[bPiece][0];
							newBlackPieces[skip][1] = blackPieces[bPiece][1];

						}
						skip++;
					}
					newWhitePieces[piece][1] = possibleMoves[move];
					if(solve(m + 1, mLimit, newWhitePieces, wLength, newBlackPieces, bLength-1)){
						return 1;
					}else{
						continue;
					}
				}
			}
		}
		return 0;
	}else{
		for(int piece = 0; piece < bLength; piece++){
			vector<int> possibleMoves;
			moves(blackPieces[piece][1], blackPieces[piece][0], &possibleMoves, blackPieces, bLength, whitePieces, wLength);
			for(int move = 0; move < possibleMoves.size(); move++){
				int newBlackPieces[bLength][2];
				copyArray(blackPieces, newBlackPieces, bLength);
				newBlackPieces[piece][1] = possibleMoves[move];
				int capture = doesCapture(possibleMoves[move], whitePieces, wLength);
				if(capture == -1){
					int newWhitePieces[wLength][2];
					copyArray(whitePieces, newWhitePieces, wLength);
					if(solve(m + 1, mLimit, newWhitePieces, wLength, newBlackPieces, bLength)){
						continue;
					}else{
						return 0;
					}
				}else{
					if(wLength - 1 == 0){
						return 0;
					}
					int newWhitePieces[wLength-1][2];
					int skip = 0;
					for(int wPiece = 0; wPiece < wLength; wPiece++){
						if(wPiece == capture){
							continue;
						}else{
							newWhitePieces[skip][0] = whitePieces[wPiece][0];
							newWhitePieces[skip][1] = whitePieces[wPiece][1];
						}
						skip++;
					}
					newBlackPieces[piece][1] = possibleMoves[move];
					if(solve(m + 1, mLimit, newWhitePieces, wLength - 1, newBlackPieces, bLength)){
						continue;
					}else{
						return 0;
					}

				}
			}
		}
		return 1;
	}
}

int main(void){
	int games;
	cin >> games;
	int w, b, m;
	for(int i = 0; i < games; i++){
		cin >> w >> b >> m;
		char k, c, r;
		int whitePieces[w][2];
		memset(whitePieces, 0, sizeof(whitePieces));
		int blackPieces[b][2];
		memset(blackPieces, 0, sizeof(blackPieces));
		for(int j = 0; j < (w + b); j++){
			cin >> k >> c >> r;
			if(j < w){
				placePiece(k, c, r, whitePieces, j);
			}else{
				placePiece(k, c, r, blackPieces, j - w);
			}
		}
		int (*pWhitePieces)[2] = whitePieces;
		int (*pBlackPieces)[2] = blackPieces;
		if(solve(1, m, pWhitePieces, w, pBlackPieces, b)){
			cout << "YES" << endl;
		}else{
			cout << "NO" << endl;
		}

	}
}

