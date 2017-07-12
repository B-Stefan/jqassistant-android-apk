@echo off
set BIN_DIR=%~dp0%
@if "%JQASSISTANT_HOME%" == ""  (
  set JQASSISTANT_HOME=%BIN_DIR%\..
)
set LIB_DIR=%JQASSISTANT_HOME%\lib
java %JQASSISTANT_OPTS% -jar "%LIB_DIR%\com.buschmais.jqassistant-commandline-1.2.0.jar" %*
