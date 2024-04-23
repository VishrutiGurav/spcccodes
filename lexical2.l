/*Definition Section*/
%{
#include<stdio.h>
%}

/* Rules Section */
%%
[\t ]+ ;
[0-9]+|[0-9]*\.[0-9]+ { printf("\n%s is NUMBER", yytext);}
#.* { printf("\n%s is COMMENT", yytext);}
[a-zA-Z][a-zA-Z0-9]+ { printf("\n%s is IDENTIFIER", yytext);}
\"[^ \"\n]*\" { printf("\n%s is STRING", yytext);}
\n { ECHO;}
%%

/* User Subroutine section */
int main()
{
	while( yylex());
}

int yywrap( )
{
	return 1;
}





/* commands */
/* flex filename.l */
/* gcc lex.yy.c */
/* a.exe */