import logging

log = logging.getLogger('collector')


class LeaderElector:
    """
    Uses the Kubernetes endpoint API to elect a leader among agents.
    This is based on the mechanism described here:
    TODO: find that link

    The election process goes like this:
    - all agents share the same endpoint name that they will try and lock
    by overriding its metadata.
    - if the endpoint doesn't exist or if its last refresh is too old
      create or update it with fresh metadata and become the leader
    - if the endpoint is already locked, there is already a leader agent. Then do nothing

    This process is triggered regularly (more frequently than the expiration period).
    The leader needs to refresh its status by overriding the timestamp in the endpoint meta.
    """

    def __init__(self, kubeutil):
        pass
