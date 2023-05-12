-- GeNeRaTeD fOr: spoofax-workspace/My-Languages/CIVIC-definition/CIVIC-cbs/CIVIC/CIVIC-Funcons/CIVIC-Funcons.cbs
{-# LANGUAGE OverloadedStrings #-}

module Funcons.CIVIC.CIVICFuncons.CIVICFuncons where

import Funcons.EDSL

import Funcons.Operations hiding (Values,libFromList)
entities = []

types = typeEnvFromList
    []

funcons = libFromList
    [("sl-to-string",StrictFuncon stepSl_to_string),("integer-add-else-string-append",StrictFuncon stepInteger_add_else_string_append),("int",StrictFuncon stepInt),("bool",StrictFuncon stepBool),("str",StrictFuncon stepStr),("obj",StrictFuncon stepObj),("fun",StrictFuncon stepFun),("scope-closed",PartiallyStrictFuncon [Strict,NonStrict] NonStrict stepScope_closed),("initialise-local-variables",NullaryFuncon stepInitialise_local_variables),("local-variable",StrictFuncon stepLocal_variable),("local-variable-initialise",StrictFuncon stepLocal_variable_initialise),("local-variable-assign",StrictFuncon stepLocal_variable_assign),("initialise-global-bindings",NullaryFuncon stepInitialise_global_bindings),("override-global-bindings",StrictFuncon stepOverride_global_bindings),("global-bound",StrictFuncon stepGlobal_bound),("read-line",NullaryFuncon stepRead_line),("print-line",StrictFuncon stepPrint_line)]

sl_to_string_ fargs = FApp "sl-to-string" (fargs)
stepSl_to_string fargs =
    evalRules [rewrite1,rewrite2] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [PADT "null-value" []] env
            rewriteTermTo (TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 117)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 108)])]))) env
          rewrite2 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V") (TSortComplement (TName "null-type"))] env
            rewriteTermTo (TApp "to-string" [TVar "V"]) env

integer_add_else_string_append_ fargs = FApp "integer-add-else-string-append" (fargs)
stepInteger_add_else_string_append fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V1") (TName "sl-values"),VPAnnotated (VPMetaVar "V2") (TName "sl-values")] env
            rewriteTermTo (TApp "else" [TApp "integer-add" [TApp "int" [TVar "V1"],TApp "int" [TVar "V2"]],TApp "string-append" [TApp "sl-to-string" [TVar "V1"],TApp "sl-to-string" [TVar "V2"]]]) env

int_ fargs = FApp "int" (fargs)
stepInt fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "sl-values")] env
            rewriteTermTo (TApp "checked" [TApp "cast-to-type" [TVar "V",TName "integers"]]) env

bool_ fargs = FApp "bool" (fargs)
stepBool fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "sl-values")] env
            rewriteTermTo (TApp "checked" [TApp "cast-to-type" [TVar "V",TName "booleans"]]) env

str_ fargs = FApp "str" (fargs)
stepStr fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "sl-values")] env
            rewriteTermTo (TApp "checked" [TApp "cast-to-type" [TVar "V",TName "strings"]]) env

obj_ fargs = FApp "obj" (fargs)
stepObj fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "sl-values")] env
            rewriteTermTo (TApp "checked" [TApp "cast-to-type" [TVar "V",TName "objects"]]) env

fun_ fargs = FApp "fun" (fargs)
stepFun fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "values")] env
            rewriteTermTo (TApp "checked" [TApp "cast-to-type" [TVar "V",TApp "functions" [TSortSeq (TName "values") QuestionMarkOp,TSortSeq (TName "values") QuestionMarkOp]]]) env

scope_closed_ fargs = FApp "scope-closed" (fargs)
stepScope_closed fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- fsMatch fargs [PAnnotated (PMetaVar "Env") (TName "envs"),PMetaVar "X"] env
            rewriteTermTo (TApp "closed" [TApp "scope" [TVar "Env",TVar "X"]]) env

initialise_local_variables_ = FName "initialise-local-variables"
stepInitialise_local_variables = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TApp "bind" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 99)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 118)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 114)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 115)])])),TApp "allocate-initialised-variable" [TName "environments",TApp "map" []]]) env

local_variable_ fargs = FApp "local-variable" (fargs)
stepLocal_variable fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "I") (TName "ids")] env
            rewriteTermTo (TApp "checked" [TApp "lookup" [TApp "assigned" [TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 99)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 118)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 114)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 115)])]))]],TVar "I"]]) env

local_variable_initialise_ fargs = FApp "local-variable-initialise" (fargs)
stepLocal_variable_initialise fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "I") (TName "ids"),VPAnnotated (VPMetaVar "V") (TName "values")] env
            rewriteTermTo (TApp "assign" [TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 99)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 118)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 114)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 115)])]))],TApp "map-override" [TMap [TBinding (TVar "I") (TApp "allocate-initialised-variable" [TName "values",TVar "V"])],TApp "assigned" [TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 99)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 118)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 114)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 115)])]))]]]]) env

local_variable_assign_ fargs = FApp "local-variable-assign" (fargs)
stepLocal_variable_assign fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "I") (TName "ids"),VPAnnotated (VPMetaVar "V") (TName "values")] env
            rewriteTermTo (TApp "else" [TApp "assign" [TApp "local-variable" [TVar "I"],TVar "V"],TApp "local-variable-initialise" [TVar "I",TVar "V"]]) env

initialise_global_bindings_ = FName "initialise-global-bindings"
stepInitialise_global_bindings = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TApp "bind" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 103)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 100)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 103)]),FValue (ADTVal "unicode-character" [FValue (Int 115)])])),TApp "allocate-initialised-variable" [TName "environments",TApp "map" []]]) env

override_global_bindings_ fargs = FApp "override-global-bindings" (fargs)
stepOverride_global_bindings fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "E") (TName "environments")] env
            rewriteTermTo (TApp "assign" [TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 103)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 100)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 103)]),FValue (ADTVal "unicode-character" [FValue (Int 115)])]))],TApp "map-override" [TVar "E",TApp "assigned" [TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 103)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 100)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 103)]),FValue (ADTVal "unicode-character" [FValue (Int 115)])]))]]]]) env

global_bound_ fargs = FApp "global-bound" (fargs)
stepGlobal_bound fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "I") (TName "ids")] env
            rewriteTermTo (TApp "checked" [TApp "lookup" [TApp "assigned" [TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 103)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 98)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 100)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 103)]),FValue (ADTVal "unicode-character" [FValue (Int 115)])]))]],TVar "I"]]) env

read_line_ = FName "read-line"
stepRead_line = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TApp "give" [TName "read",TApp "if-true-else" [TApp "is-eq" [TName "given",TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 92)]),FValue (ADTVal "unicode-character" [FValue (Int 110)])]))],TName "nil",TApp "cons" [TName "given",TName "read-line"]]]) env

print_line_ fargs = FApp "print-line" (fargs)
stepPrint_line fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "S") (TName "strings")] env
            rewriteTermTo (TApp "print" [TVar "S",TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 10)])]))]) env