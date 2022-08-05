#include "StdAfx.h"

#ifdef ENABLE_BIOLOG_SYSTEM
#include "PythonBiologManager.h"
/*******************************************************************\
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||| CPythonBiologManager - CLASS
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
\*******************************************************************/

/*******************************************************************\
| [PUBLIC] (De-)Initialize Functions
\*******************************************************************/
CPythonBiologManager::CPythonBiologManager()
{
	Initialize();
}

CPythonBiologManager::~CPythonBiologManager()
{

}

void CPythonBiologManager::Initialize()
{
	ZeroMemory(&m_BiologInfo, sizeof(m_BiologInfo));
}

/*******************************************************************\
| [PUBLIC] Highscore Functions
\*******************************************************************/
void CPythonBiologManager::_LoadBiologInformation(const TPacketGCBiologManagerInfo* pBiologInfo)
{
	memcpy(&m_BiologInfo, pBiologInfo, sizeof(m_BiologInfo));
}
#endif
