-- GeNeRaTeD fOr: spoofax-workspace/My-Languages/CIVIC-definition/CIVIC-cbs/CIVIC/CIVIC-Funcons/CIVIC-Funcons.cbs
{-# LANGUAGE OverloadedStrings #-}

module Funcons.CIVIC.CIVICFuncons.CIVICFuncons where

import Funcons.EDSL

import Funcons.Operations hiding (Values,libFromList)
entities = []

types = typeEnvFromList
    [("shared-state-features",DataTypeMemberss "shared-state-features" [] [DataTypeMemberConstructor "cv" [] (Just []),DataTypeMemberConstructor "mtx" [] (Just []),DataTypeMemberConstructor "state" [] (Just []),DataTypeMemberConstructor "is-set" [] (Just [])])]

funcons = libFromList
    [("print-debug",NullaryFuncon stepPrint_debug),("overload-multithread",NonStrictFuncon stepOverload_multithread),("condition-wait-with-lock-overload",StrictFuncon stepCondition_wait_with_lock_overload),("overload-initialise-multithreading",NullaryFuncon stepOverload_initialise_multithreading),("values-or-thread-ids",NullaryFuncon stepValues_or_thread_ids),("foreach-thread-try-wake",StrictFuncon stepForeach_thread_try_wake),("sleeping-threads-lowest-v",StrictFuncon stepSleeping_threads_lowest_v),("try-wake",StrictFuncon stepTry_wake),("force-wake",StrictFuncon stepForce_wake),("thread-sleep",StrictFuncon stepThread_sleep),("all-values",NullaryFuncon stepAll_values),("method-zero-params",NonStrictFuncon stepMethod_zero_params),("self",StrictFuncon stepSelf),("method",NonStrictFuncon stepMethod),("unpack",StrictFuncon stepUnpack),("simple-class",StrictFuncon stepSimple_class),("extend-object-map",StrictFuncon stepExtend_object_map),("get-class-method",StrictFuncon stepGet_class_method),("values-or-syncs",NullaryFuncon stepValues_or_syncs),("cv",NullaryFuncon stepCv),("mtx",NullaryFuncon stepMtx),("state",NullaryFuncon stepState),("is-set",NullaryFuncon stepIs_set),("shared-state",NullaryFuncon stepShared_state),("shared-state-create",NullaryFuncon stepShared_state_create),("shared-state-get",StrictFuncon stepShared_state_get),("shared-state-set",StrictFuncon stepShared_state_set),("tuple-head",StrictFuncon stepTuple_head),("tuple-tail",StrictFuncon stepTuple_tail),("initialise-n-steps",NullaryFuncon stepInitialise_n_steps),("current-n-steps",NullaryFuncon stepCurrent_n_steps),("n-steps-set",StrictFuncon stepN_steps_set),("increment-n-steps",NullaryFuncon stepIncrement_n_steps),("initialise-sleep-map",NullaryFuncon stepInitialise_sleep_map),("add-to-sleep-map",StrictFuncon stepAdd_to_sleep_map),("remove-from-sleep-map",StrictFuncon stepRemove_from_sleep_map),("current-sleep-map",NullaryFuncon stepCurrent_sleep_map),("is-some-thread-sleeping",NullaryFuncon stepIs_some_thread_sleeping),("set-size-active-thread-set",NullaryFuncon stepSet_size_active_thread_set),("current-active-thread-set",NullaryFuncon stepCurrent_active_thread_set),("current-thread-stepping",NullaryFuncon stepCurrent_thread_stepping),("thread-resume-no-checks",StrictFuncon stepThread_resume_no_checks),("thread-wake",StrictFuncon stepThread_wake),("overload-condition-notify-all",StrictFuncon stepOverload_condition_notify_all),("shared-state-features",NullaryFuncon stepShared_state_features)]

print_debug_ = FName "print-debug"
stepPrint_debug = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TName "false") env

overload_multithread_ fargs = FApp "overload-multithread" (fargs)
stepOverload_multithread fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- fsMatch fargs [PMetaVar "X"] env
            rewriteTermTo (TApp "sequential" [TName "overload-initialise-multithreading",TApp "give" [TApp "thread-activate" [TApp "thread-joinable" [TApp "thunk" [TApp "closure" [TVar "X"]]]],TApp "handle-abrupt" [TApp "sequential" [TApp "while-true" [TApp "or" [TName "is-some-thread-active",TName "is-some-thread-sleeping"],TApp "sequential" [TApp "if-else" [TApp "and" [TApp "is-equal" [TApp "set-size" [TName "current-active-thread-set"],TFuncon (FValue (Nat 0))],TName "is-some-thread-sleeping"],TApp "force-wake" [TApp "tuple-elements" [TApp "sleeping-threads-lowest-v" [TApp "map-elements" [TName "current-sleep-map"]]]],TName "null"],TName "update-thread-stepping",TApp "sequential" [TApp "handle-abrupt" [TName "thread-step",TApp "sequential" [TApp "print" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 104)]),FValue (ADTVal "unicode-character" [FValue (Int 114)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 100)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 115)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 112)]),FValue (ADTVal "unicode-character" [FValue (Int 32)]),FValue (ADTVal "unicode-character" [FValue (Int 102)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 100)])]))]]],TName "increment-n-steps",TApp "foreach-thread-try-wake" [TApp "map-elements" [TName "current-sleep-map"]]]]],TApp "handle-abrupt" [TApp "check" [TApp "not" [TName "is-some-thread-suspended"]],TApp "abrupt" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 100)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 100)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 99)]),FValue (ADTVal "unicode-character" [FValue (Int 107)])]))]],TApp "thread-value" [TName "given"]],TName "given"]]]) env

condition_wait_with_lock_overload_ fargs = FApp "condition-wait-with-lock-overload" (fargs)
stepCondition_wait_with_lock_overload fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "SY") (TName "syncs"),VPAnnotated (VPMetaVar "L") (TName "syncs")] env
            rewriteTermTo (TApp "sequential" [TApp "thread-atomic" [TApp "sequential" [TApp "exclusive-lock-release" [TVar "L"],TApp "sync-waiting-list-add" [TVar "SY",TName "current-thread"],TApp "thread-suspend" [TName "current-thread"]]],TApp "exclusive-lock-sync-else-wait" [TVar "L"]]) env

overload_initialise_multithreading_ = FName "overload-initialise-multithreading"
stepOverload_initialise_multithreading = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TApp "sequential" [TName "initialise-thread-map",TName "initialise-active-thread-set",TName "initialise-thread-stepping",TName "initialise-terminated-thread-map",TName "initialise-thread-schedule",TName "initialise-n-steps",TName "initialise-sleep-map"]) env

values_or_thread_ids_ = FName "values-or-thread-ids"
stepValues_or_thread_ids = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TSortUnion (TName "thread-ids") (TName "values")) env

foreach_thread_try_wake_ fargs = FApp "foreach-thread-try-wake" (fargs)
stepForeach_thread_try_wake fargs =
    evalRules [rewrite1,rewrite2] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [] env
            rewriteTermTo (TName "null") env
          rewrite2 = do
            let env = emptyEnv
            env <- vsMatch fargs [PADT "tuple" [VPAnnotated (VPMetaVar "V") (TName "ints"),VPAnnotated (VPMetaVar "S") (TName "syncs")],VPAnnotated (VPSeqVar "T*" StarOp) (TSortSeq (TApp "tuples" [TName "ints",TName "syncs"]) StarOp)] env
            rewriteTermTo (TApp "sequential" [TApp "try-wake" [TVar "V",TVar "S"],TApp "foreach-thread-try-wake" [TVar "T*"]]) env

sleeping_threads_lowest_v_ fargs = FApp "sleeping-threads-lowest-v" (fargs)
stepSleeping_threads_lowest_v fargs =
    evalRules [rewrite1,rewrite2,rewrite3] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [] env
            rewriteTermTo (TApp "tuple" []) env
          rewrite2 = do
            let env = emptyEnv
            env <- vsMatch fargs [PADT "tuple" [VPAnnotated (VPMetaVar "V") (TName "ints"),VPAnnotated (VPMetaVar "S") (TName "syncs")]] env
            rewriteTermTo (TApp "tuple" [TVar "V",TVar "S"]) env
          rewrite3 = do
            let env = emptyEnv
            env <- vsMatch fargs [PADT "tuple" [VPAnnotated (VPMetaVar "V1") (TName "ints"),VPAnnotated (VPMetaVar "S1") (TName "syncs")],PADT "tuple" [VPAnnotated (VPMetaVar "V2") (TName "ints"),VPAnnotated (VPMetaVar "S2") (TName "syncs")],VPAnnotated (VPSeqVar "T*" StarOp) (TSortSeq (TApp "tuples" [TName "ints",TName "syncs"]) StarOp)] env
            rewriteTermTo (TApp "sequential" [TApp "if-else" [TApp "is-less" [TVar "V2",TVar "V1"],TApp "sleeping-threads-lowest-v" [TApp "tuple" [TVar "V2",TVar "S2"],TVar "T*"],TApp "sleeping-threads-lowest-v" [TApp "tuple" [TVar "V1",TVar "S1"],TVar "T*"]]]) env

try_wake_ fargs = FApp "try-wake" (fargs)
stepTry_wake fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "ints"),VPAnnotated (VPMetaVar "S") (TName "syncs")] env
            rewriteTermTo (TApp "sequential" [TApp "if-else" [TApp "is-greater-or-equal" [TName "current-n-steps",TVar "V"],TApp "sequential" [TApp "thread-wake" [TVar "V",TVar "S"]],TName "null"]]) env

force_wake_ fargs = FApp "force-wake" (fargs)
stepForce_wake fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "ints"),VPAnnotated (VPMetaVar "S") (TName "syncs")] env
            rewriteTermTo (TApp "sequential" [TApp "n-steps-set" [TVar "V"],TApp "thread-wake" [TVar "V",TVar "S"]]) env

thread_sleep_ fargs = FApp "thread-sleep" (fargs)
stepThread_sleep fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "ints")] env
            rewriteTermTo (TApp "thread-atomic" [TApp "sequential" [TApp "closed" [TApp "scope" [TMap [TBinding (TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 119)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 107)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 109)]),FValue (ADTVal "unicode-character" [FValue (Int 101)])]))) (TApp "integer-add" [TVar "V",TName "current-n-steps"]),TBinding (TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 99)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 100)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 110)])]))) (TName "condition-create")],TApp "sequential" [TApp "print" [TFuncon (FValue (ADTVal "list" []))],TApp "if-else" [TApp "is-equal" [TApp "tuple" [TApp "lookup" [TName "current-sleep-map",TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 119)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 107)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 109)]),FValue (ADTVal "unicode-character" [FValue (Int 101)])]))]]],TApp "tuple" []],TApp "thread-atomic" [TApp "sequential" [TApp "add-to-sleep-map" [TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 119)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 107)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 109)]),FValue (ADTVal "unicode-character" [FValue (Int 101)])]))],TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 99)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 100)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 110)])]))]],TApp "condition-wait" [TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 99)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 100)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 110)])]))]]]],TApp "condition-wait" [TApp "lookup" [TName "current-sleep-map",TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 119)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 107)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 109)]),FValue (ADTVal "unicode-character" [FValue (Int 101)])]))]]]]]]]]]) env

all_values_ = FName "all-values"
stepAll_values = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TSortUnion (TSortUnion (TApp "functions" [TApp "tuples" [TSortSeq (TName "values") StarOp],TName "values"]) (TName "values")) (TName "syncs")) env

method_zero_params_ fargs = FApp "method-zero-params" (fargs)
stepMethod_zero_params fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- fsMatch fargs [PMetaVar "X"] env
            rewriteTermTo (TApp "function" [TApp "closure" [TApp "scope" [TApp "collateral" [TApp "match" [TName "given",TApp "tuple" [TApp "pattern" [TApp "abstraction" [TMap [TBinding (TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 115)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 102)])]))) (TApp "allocate-initialised-variable" [TApp "pointers" [TName "objects"],TName "given"])]]]]],TApp "object-single-inheritance-feature-map" [TApp "checked" [TApp "dereference" [TApp "first" [TApp "tuple-elements" [TName "given"]]]]]],TApp "sequential" [TVar "X"]]]]) env

self_ fargs = FApp "self" (fargs)
stepSelf fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "I") (TName "ids")] env
            rewriteTermTo (TApp "lookup" [TApp "object-single-inheritance-feature-map" [TApp "checked" [TApp "dereference" [TApp "assigned" [TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 115)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 102)])]))]]]]],TVar "I"]) env

method_ fargs = FApp "method" (fargs)
stepMethod fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- fsMatch fargs [PMetaVar "X",PSeqVar "U?" QuestionMarkOp] env
            rewriteTermTo (TApp "function" [TApp "closure" [TApp "scope" [TApp "collateral" [TApp "match" [TName "given",TApp "tuple" [TApp "pattern" [TApp "abstraction" [TMap [TBinding (TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 115)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 108)]),FValue (ADTVal "unicode-character" [FValue (Int 102)])]))) (TApp "allocate-initialised-variable" [TApp "pointers" [TName "objects"],TName "given"])]]],TVar "U?"]],TApp "object-single-inheritance-feature-map" [TApp "checked" [TApp "dereference" [TApp "first" [TApp "tuple-elements" [TName "given"]]]]]],TApp "handle-return" [TApp "sequential" [TVar "X"]]]]]) env

unpack_ fargs = FApp "unpack" (fargs)
stepUnpack fargs =
    evalRules [rewrite1,rewrite2] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "I") (TName "ids"),VPAnnotated (VPSeqVar "I*" StarOp) (TSortSeq (TName "ids") StarOp)] env
            rewriteTermTo (TSeq [TApp "pattern" [TApp "abstraction" [TApp "bind" [TVar "I",TApp "alloc-init" [TName "values",TName "given"]]]],TApp "unpack" [TVar "I*"]]) env
          rewrite2 = do
            let env = emptyEnv
            env <- vsMatch fargs [] env
            rewriteTermTo (TSeq []) env

simple_class_ fargs = FApp "simple-class" (fargs)
stepSimple_class fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "I") (TName "ids"),VPAnnotated (VPMetaVar "V") (TName "envs"),VPAnnotated (VPMetaVar "F") (TName "envs")] env
            rewriteTermTo (TApp "class" [TApp "thunk" [TApp "closure" [TApp "reference" [TApp "object" [TName "fresh-atom",TVar "I",TVar "V"]]]],TVar "F"]) env

extend_object_map_ fargs = FApp "extend-object-map" (fargs)
stepExtend_object_map fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "O") (TName "objects"),VPAnnotated (VPMetaVar "Env") (TName "environments")] env
            rewriteTermTo (TApp "object" [TName "fresh-atom",TApp "object-class-name" [TVar "O"],TApp "map-unite" [TApp "object-feature-map" [TVar "O"],TVar "Env"]]) env

get_class_method_ fargs = FApp "get-class-method" (fargs)
stepGet_class_method fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "O") (TName "objects"),VPAnnotated (VPMetaVar "I") (TName "ids")] env
            rewriteTermTo (TApp "checked" [TApp "lookup" [TApp "class-feature-map" [TApp "checked" [TApp "lookup" [TApp "assigned" [TApp "bound" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 95)]),FValue (ADTVal "unicode-character" [FValue (Int 115)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 100)])]))]],TApp "object-class-name" [TVar "O"]]]],TVar "I"]]) env

values_or_syncs_ = FName "values-or-syncs"
stepValues_or_syncs = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TSortUnion (TName "values") (TName "syncs")) env

cv_ = FName "cv"
stepCv = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TApp "datatype-value" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 99)]),FValue (ADTVal "unicode-character" [FValue (Int 118)])]))]) env

mtx_ = FName "mtx"
stepMtx = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TApp "datatype-value" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 109)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 120)])]))]) env

state_ = FName "state"
stepState = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TApp "datatype-value" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 115)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 101)])]))]) env

is_set_ = FName "is-set"
stepIs_set = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TApp "datatype-value" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 115)]),FValue (ADTVal "unicode-character" [FValue (Int 45)]),FValue (ADTVal "unicode-character" [FValue (Int 115)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 116)])]))]) env

shared_state_ = FName "shared-state"
stepShared_state = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TApp "maps" [TName "shared-state-features",TName "values-or-syncs"]) env

shared_state_create_ = FName "shared-state-create"
stepShared_state_create = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TMap [TBinding (TName "cv") (TApp "allocate-initialised-variable" [TName "syncs",TName "condition-create"]),TBinding (TName "mtx") (TApp "allocate-initialised-variable" [TName "syncs",TName "exclusive-lock-create"]),TBinding (TName "state") (TApp "allocate-initialised-variable" [TName "values",TName "null"]),TBinding (TName "is-set") (TApp "allocate-initialised-variable" [TName "booleans",TName "false"])]) env

shared_state_get_ fargs = FApp "shared-state-get" (fargs)
stepShared_state_get fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "P") (TName "shared-state")] env
            rewriteTermTo (TApp "if-else" [TApp "assigned" [TApp "checked" [TApp "map-lookup" [TVar "P",TName "is-set"]]],TApp "assigned" [TApp "checked" [TApp "map-lookup" [TVar "P",TName "state"]]],TApp "sequential" [TApp "print" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 119)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 103)])]))],TApp "condition-wait" [TApp "assigned" [TApp "checked" [TApp "map-lookup" [TVar "P",TName "cv"]]]],TApp "print" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 119)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 115)]),FValue (ADTVal "unicode-character" [FValue (Int 32)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 102)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 100)])]))],TApp "assigned" [TApp "checked" [TApp "map-lookup" [TVar "P",TName "state"]]]]]) env

shared_state_set_ fargs = FApp "shared-state-set" (fargs)
stepShared_state_set fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "P") (TName "shared-state"),VPAnnotated (VPMetaVar "V") (TName "values")] env
            rewriteTermTo (TApp "thread-atomic" [TApp "if-else" [TApp "assigned" [TApp "checked" [TApp "map-lookup" [TVar "P",TName "is-set"]]],TApp "print" [TName "null"],TApp "thread-atomic" [TApp "sequential" [TApp "assign" [TApp "checked" [TApp "map-lookup" [TVar "P",TName "state"]],TVar "V"],TApp "assign" [TApp "checked" [TApp "map-lookup" [TVar "P",TName "is-set"]],TName "true"],TApp "condition-notify-all" [TApp "assigned" [TApp "checked" [TApp "map-lookup" [TVar "P",TName "cv"]]]],TApp "print" [TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 104)]),FValue (ADTVal "unicode-character" [FValue (Int 97)]),FValue (ADTVal "unicode-character" [FValue (Int 115)]),FValue (ADTVal "unicode-character" [FValue (Int 32)]),FValue (ADTVal "unicode-character" [FValue (Int 110)]),FValue (ADTVal "unicode-character" [FValue (Int 111)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 102)]),FValue (ADTVal "unicode-character" [FValue (Int 105)]),FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 100)])]))]]]]]) env

tuple_head_ fargs = FApp "tuple-head" (fargs)
stepTuple_head fargs =
    evalRules [rewrite1,rewrite2] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [PADT "tuple" []] env
            rewriteTermTo (TSeq []) env
          rewrite2 = do
            let env = emptyEnv
            env <- vsMatch fargs [PADT "tuple" [VPAnnotated (VPMetaVar "V") (TName "values"),VPAnnotated (VPSeqVar "V*" StarOp) (TSortSeq (TName "values") StarOp)]] env
            rewriteTermTo (TVar "V") env

tuple_tail_ fargs = FApp "tuple-tail" (fargs)
stepTuple_tail fargs =
    evalRules [rewrite1,rewrite2] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [PADT "tuple" []] env
            rewriteTermTo (TSeq []) env
          rewrite2 = do
            let env = emptyEnv
            env <- vsMatch fargs [PADT "tuple" [VPAnnotated (VPMetaVar "V") (TName "values"),VPAnnotated (VPSeqVar "V*" StarOp) (TSortSeq (TName "values") StarOp)]] env
            rewriteTermTo (TApp "tuple" [TVar "V*"]) env

initialise_n_steps_ = FName "initialise-n-steps"
stepInitialise_n_steps = evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            putMutTerm "n-steps" (TFuncon (FValue (Nat 0))) env
            stepTermTo (TName "null-value") env

current_n_steps_ = FName "current-n-steps"
stepCurrent_n_steps = evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            env <- getMutPatt "n-steps" [VPMetaVar "T"] env
            stepTermTo (TVar "T") env

n_steps_set_ fargs = FApp "n-steps-set" (fargs)
stepN_steps_set fargs =
    evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            env <- lifted_vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "ints")] env
            env <- getMutPatt "n-steps" [VPMetaVar "T"] env
            putMutTerm "n-steps" (TVar "V") env
            stepTermTo (TName "null") env

increment_n_steps_ = FName "increment-n-steps"
stepIncrement_n_steps = evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            env <- getMutPatt "n-steps" [VPMetaVar "T"] env
            putMutTerm "n-steps" (TApp "nat-succ" [TVar "T"]) env
            stepTermTo (TName "null") env

initialise_sleep_map_ = FName "initialise-sleep-map"
stepInitialise_sleep_map = evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            putMutTerm "sleep-map" (TApp "map" []) env
            stepTermTo (TName "null-value") env

add_to_sleep_map_ fargs = FApp "add-to-sleep-map" (fargs)
stepAdd_to_sleep_map fargs =
    evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            env <- lifted_vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "ints"),VPAnnotated (VPMetaVar "S") (TName "syncs")] env
            env <- getMutPatt "sleep-map" [VPMetaVar "M"] env
            putMutTerm "sleep-map" (TApp "map-unite" [TMap [TBinding (TVar "V") (TVar "S")],TVar "M"]) env
            stepTermTo (TName "null-value") env

remove_from_sleep_map_ fargs = FApp "remove-from-sleep-map" (fargs)
stepRemove_from_sleep_map fargs =
    evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            env <- lifted_vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "ints")] env
            env <- getMutPatt "sleep-map" [VPMetaVar "M"] env
            putMutTerm "sleep-map" (TApp "map-delete" [TVar "M",TApp "set" [TVar "V"]]) env
            stepTermTo (TName "null-value") env

current_sleep_map_ = FName "current-sleep-map"
stepCurrent_sleep_map = evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            env <- getMutPatt "sleep-map" [VPMetaVar "M"] env
            stepTermTo (TVar "M") env

is_some_thread_sleeping_ = FName "is-some-thread-sleeping"
stepIs_some_thread_sleeping = evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            rewriteTermTo (TApp "not" [TApp "is-equal" [TApp "tuple" [TApp "map-elements" [TName "current-sleep-map"]],TApp "tuple" []]]) env

set_size_active_thread_set_ = FName "set-size-active-thread-set"
stepSet_size_active_thread_set = evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            env <- getMutPatt "active-thread-set" [VPMetaVar "ATS"] env
            stepTermTo (TApp "set-size" [TVar "ATS"]) env

current_active_thread_set_ = FName "current-active-thread-set"
stepCurrent_active_thread_set = evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            env <- getMutPatt "active-thread-set" [VPMetaVar "M"] env
            stepTermTo (TVar "M") env

current_thread_stepping_ = FName "current-thread-stepping"
stepCurrent_thread_stepping = evalRules [] [step1,step2]
    where step1 = do
            let env = emptyEnv
            env <- getMutPatt "thread-stepping" [VPMetaVar "TI"] env
            stepTermTo (TVar "TI") env
          step2 = do
            let env = emptyEnv
            env <- getMutPatt "thread-stepping" [] env
            stepTermTo (TFuncon (FValue (ADTVal "list" [FValue (ADTVal "unicode-character" [FValue (Int 101)]),FValue (ADTVal "unicode-character" [FValue (Int 109)]),FValue (ADTVal "unicode-character" [FValue (Int 112)]),FValue (ADTVal "unicode-character" [FValue (Int 116)]),FValue (ADTVal "unicode-character" [FValue (Int 121)])]))) env

thread_resume_no_checks_ fargs = FApp "thread-resume-no-checks" (fargs)
stepThread_resume_no_checks fargs =
    evalRules [] [step1]
    where step1 = do
            let env = emptyEnv
            env <- lifted_vsMatch fargs [VPAnnotated (VPSeqVar "TI*" StarOp) (TSortSeq (TName "thread-ids") StarOp)] env
            env <- getMutPatt "active-thread-set" [VPMetaVar "ATS"] env
            putMutTerm "active-thread-set" (TApp "set-unite" [TVar "ATS",TSet [TVar "TI*"]]) env
            stepTermTo (TName "null-value") env

thread_wake_ fargs = FApp "thread-wake" (fargs)
stepThread_wake fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "V") (TName "ints"),VPAnnotated (VPMetaVar "S") (TName "syncs")] env
            rewriteTermTo (TApp "sequential" [TApp "remove-from-sleep-map" [TVar "V"],TApp "overload-condition-notify-all" [TVar "S"]]) env

overload_condition_notify_all_ fargs = FApp "overload-condition-notify-all" (fargs)
stepOverload_condition_notify_all fargs =
    evalRules [rewrite1] []
    where rewrite1 = do
            let env = emptyEnv
            env <- vsMatch fargs [VPAnnotated (VPMetaVar "SY") (TName "syncs")] env
            rewriteTermTo (TApp "sequential" [TApp "thread-resume-no-checks" [TApp "list-elements" [TApp "assigned" [TApp "sync-feature" [TVar "SY",TName "sync-waiting-list"]]]],TApp "assign" [TApp "sync-feature" [TVar "SY",TName "sync-waiting-list"],TApp "list" []]]) env

shared_state_features_ = FName "shared-state-features"
stepShared_state_features = rewriteType "shared-state-features" []