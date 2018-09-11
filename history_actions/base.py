POST_SAVE_MODEL_SIGNAL = 'POST_SAVE_MODEL_SIGNAL'
PRE_SAVE_MODEL_SIGNAL = 'PRE_SAVE_MODEL_SIGNAL'
PRE_DELETE_MODEL_SIGNAL = 'PRE_DELETE_MODEL_SIGNAL'
POST_DELETE_MODEL_SIGNAL = 'POST_DELETE_MODEL_SIGNAL'


class BaseSignalHistory:

    @classmethod
    def save_signal_callback(cls, sender, *args, **kwargs):
        from history_actions.manager import HistoryManager

        instance = kwargs.get('instance')

        HistoryManager.create(
            'admin',
            cls.SIGNAL_TYPE,
            model_instance=instance,
            from_signal=True
        )


class PostSaveHistory(BaseSignalHistory):

    SIGNAL_TYPE = POST_SAVE_MODEL_SIGNAL


class PreSaveHistory(BaseSignalHistory):

    SIGNAL_TYPE = PRE_SAVE_MODEL_SIGNAL


class PreDeleteHistory(BaseSignalHistory):

    SIGNAL_TYPE = PRE_DELETE_MODEL_SIGNAL


class PostDeleteHistory(BaseSignalHistory):

    SIGNAL_TYPE = POST_DELETE_MODEL_SIGNAL
