create or replace function EXEC_PYTHON(script string, arg1 variant)
  returns variant
  as
  $$
   STARSNOW_REQUEST('http://<your_tabpy_server>/evaluate', 
                        OBJECT_CONSTRUCT('method','post', 'data', 
                                         OBJECT_CONSTRUCT( 'script', script, 'data',
                                                          OBJECT_CONSTRUCT('_arg1', arg1 ))  )) 
  $$
  ;
