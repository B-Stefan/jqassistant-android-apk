#!/bin/sh
if [ -z "$JQASSISTANT_HOME" ] ; then
  BIN_DIR=`dirname "$0"`
  export JQASSISTANT_HOME=`cd "$BIN_DIR/.." && pwd -P`
fi
LIB_DIR=$JQASSISTANT_HOME/lib
java $JQASSISTANT_OPTS -jar "$LIB_DIR/com.buschmais.jqassistant-commandline-1.2.0.jar" $*

